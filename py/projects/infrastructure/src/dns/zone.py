import pulumi
import pulumi_aws as aws

from .domains import BASE_DOMAIN, STACK_DOMAIN, stack

zone = aws.route53.Zone(
    resource_name="zone",
    name=STACK_DOMAIN,
    comment=f"{pulumi.get_project().capitalize()} {stack}",
)

# Create the NS records in the parent domain

if stack == "prod":
    aws.route53.Record(
        resource_name="preview",
        type="NS",
        name=f"preview.{BASE_DOMAIN}",
        records=[
            "ns-1087.awsdns-07.org",
            "ns-1606.awsdns-08.co.uk",
            "ns-249.awsdns-31.com",
            "ns-825.awsdns-39.net",
        ],
        ttl=60 * 10,
        zone_id=zone.id,
        opts=pulumi.ResourceOptions(parent=zone),
    )
