import pulumi
import pulumi_aws as aws
import pulumi_docker as docker
import pulumi_nuage.aws as nuage

repository = nuage.Repository(
    resource_name="repository",
    name=f"{pulumi.get_project()}-{pulumi.get_stack()}",
    expire_in_days=30,
)

auth = aws.ecr.get_authorization_token(registry_id=repository.registry_id)

docker_registry = docker.RegistryArgs(
    server=auth.proxy_endpoint,
    username=auth.user_name,
    password=auth.password,
)

architecture = nuage.ArchitectureType.ARM64.value
