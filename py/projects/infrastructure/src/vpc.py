import pulumi
import pulumi_aws as aws

aws_config = pulumi.Config("aws")
region = aws_config.require("region")

NAME = f"{pulumi.get_project()}-{pulumi.get_stack()}"

vpc = aws.ec2.Vpc(
    resource_name="vpc",
    cidr_block="10.0.0.0/16",
    enable_dns_hostnames=True,
    enable_dns_support=True,
    tags={"Name": NAME},
)

# Subnets

private_subnets = []
private_subnet_ids = []
for i, az in enumerate(["a", "b", "c"]):
    private_subnet = aws.ec2.Subnet(
        resource_name=f"private-{az}",
        cidr_block=f"10.0.{i}.0/24",
        vpc_id=vpc.id,
        availability_zone=f"{region}{az}",
        map_public_ip_on_launch=False,
        tags={"Name": f"{NAME}-private-{az}", "SubnetType": "private"},
        opts=pulumi.ResourceOptions(parent=vpc),
    )
    private_subnets.append(private_subnet)
    private_subnet_ids.append(private_subnet.id)

public_subnets = []
public_subnet_ids = []
for i, az in enumerate(["a", "b", "c"]):
    public_subnet = aws.ec2.Subnet(
        resource_name=f"public-{az}",
        cidr_block=f"10.0.{i+128}.0/24",
        vpc_id=vpc.id,
        availability_zone=f"{region}{az}",
        map_public_ip_on_launch=True,
        tags={"Name": f"{NAME}-public-{az}", "SubnetType": "public"},
        opts=pulumi.ResourceOptions(parent=vpc),
    )
    public_subnets.append(public_subnet)
    public_subnet_ids.append(public_subnet.id)

# NAT & Internet Gateways

nat_ip = aws.ec2.Eip(
    resource_name="nat",
    vpc=True,
    tags={"Name": NAME},
    opts=pulumi.ResourceOptions(parent=public_subnets[0]),
)

nat = aws.ec2.NatGateway(
    resource_name="nat",
    allocation_id=nat_ip.allocation_id,
    subnet_id=public_subnets[0].id,
    tags={"Name": NAME},
    opts=pulumi.ResourceOptions(parent=public_subnets[0]),
)

internet_gateway = aws.ec2.InternetGateway(
    resource_name="igw",
    vpc_id=vpc.id,
    tags={"Name": NAME},
    opts=pulumi.ResourceOptions(parent=vpc),
)

# Route tables

for private_subnet in private_subnets:
    route_table = aws.ec2.RouteTable(
        resource_name=private_subnet._name,
        vpc_id=vpc.id,
        routes=[
            aws.ec2.RouteTableRouteArgs(
                cidr_block="0.0.0.0/0",
                nat_gateway_id=nat.id,
            )
        ],
        tags=private_subnet.tags,
        opts=pulumi.ResourceOptions(parent=private_subnet),
    )

    aws.ec2.RouteTableAssociation(
        resource_name=private_subnet._name,
        subnet_id=private_subnet.id,
        route_table_id=route_table.id,
        opts=pulumi.ResourceOptions(parent=route_table),
    )

for public_subnet in public_subnets:
    route_table = aws.ec2.RouteTable(
        resource_name=public_subnet._name,
        vpc_id=vpc.id,
        routes=[
            aws.ec2.RouteTableRouteArgs(
                cidr_block="0.0.0.0/0",
                gateway_id=internet_gateway.id,
            )
        ],
        tags=public_subnet.tags,
        opts=pulumi.ResourceOptions(parent=public_subnet),
    )

    aws.ec2.RouteTableAssociation(
        resource_name=public_subnet._name,
        subnet_id=public_subnet.id,
        route_table_id=route_table.id,
        opts=pulumi.ResourceOptions(parent=route_table),
    )


open_egress_security_group = aws.ec2.SecurityGroup(
    resource_name="egress",
    name_prefix=f"egress-sg-{pulumi.get_stack()}-",
    description="Allow outbound traffic",
    vpc_id=vpc.id,
    egress=[
        aws.ec2.SecurityGroupEgressArgs(
            from_port=0,
            to_port=0,
            protocol=aws.ec2.ProtocolType.ALL,
            cidr_blocks=["0.0.0.0/0"],
        )
    ],
    opts=pulumi.ResourceOptions(parent=vpc),
)
