from urllib.parse import ParseResult, urlparse

import pulumi
import pulumi_aws as aws
import pulumi_docker as docker
import pulumi_nuage.aws as nuage

from shared.settings import FakerSettings, GraphQLSettings

from ..certificates import global_certificate, global_certificate_validation
from ..common import get_env_var_names
from ..dns.domains import ADMIN_DOMAIN
from ..dns.zone import zone
from ..ecr import docker_registry, repository

env = pulumi.get_stack()
architecture = nuage.ArchitectureType.ARM64.value

SERVICE_NAME = "admin"
SERVICE_DESCRIPTION = (
    f"{pulumi.get_project().capitalize()} GraphQL {SERVICE_NAME} API ({env})"
)

image = docker.Image(
    resource_name=SERVICE_NAME,
    image_name=repository.url.apply(lambda url: f"{url}:{SERVICE_NAME}"),
    registry=docker_registry,
    build=docker.DockerBuildArgs(
        context="../..",
        platform=f"linux/{architecture}".lower(),
        target=SERVICE_NAME,
    ),
)

function = nuage.ContainerFunction(
    resource_name=SERVICE_NAME,
    name_prefix=f"{pulumi.get_project()}-{SERVICE_NAME}-{env}",
    image_uri=image.repo_digest,  # type: ignore
    memory_size=512,
    architecture=architecture,
    environment=get_env_var_names(
        GraphQLSettings(
            powertools_service_name=SERVICE_NAME,
            faker=FakerSettings(enabled=True, seed=42),
        )
    ),
    description=SERVICE_DESCRIPTION,
    url_config=nuage.FunctionUrlArgs(
        url_enabled=True,
        cors_configuration=aws.lambda_.FunctionUrlCorsArgs(
            allow_origins=["*"],
        ),
    ),
    log_retention_in_days=7,
    keep_warm=True,
    opts=pulumi.ResourceOptions(parent=image),
)

parsed_url: pulumi.Output[ParseResult] = function.url.apply(urlparse)

function_origin = aws.cloudfront.DistributionOriginArgs(
    origin_id=SERVICE_NAME,
    domain_name=parsed_url.netloc,
    origin_path=parsed_url.path.apply(lambda path: path.rstrip("/")),
    custom_origin_config=aws.cloudfront.DistributionOriginCustomOriginConfigArgs(
        http_port=80,
        https_port=443,
        origin_protocol_policy="https-only",
        origin_ssl_protocols=["TLSv1.2"],
    ),
)

distribution = aws.cloudfront.Distribution(
    resource_name=SERVICE_NAME,
    enabled=True,
    aliases=[ADMIN_DOMAIN],
    comment=SERVICE_DESCRIPTION,
    wait_for_deployment=False,
    origins=[function_origin],
    default_cache_behavior=aws.cloudfront.DistributionDefaultCacheBehaviorArgs(
        target_origin_id=function_origin.origin_id,
        allowed_methods=[
            "DELETE",
            "GET",
            "HEAD",
            "OPTIONS",
            "PATCH",
            "POST",
            "PUT",
        ],
        cached_methods=[
            "GET",
            "HEAD",
        ],
        viewer_protocol_policy="redirect-to-https",
        origin_request_policy_id=aws.cloudfront.get_origin_request_policy(
            name="Managed-AllViewerExceptHostHeader"
        ).id,
        cache_policy_id=aws.cloudfront.get_cache_policy(
            name="Managed-CachingOptimized"
        ).id,
        compress=True,
    ),
    restrictions=aws.cloudfront.DistributionRestrictionsArgs(
        geo_restriction=aws.cloudfront.DistributionRestrictionsGeoRestrictionArgs(
            restriction_type="none"
        )
    ),
    viewer_certificate=aws.cloudfront.DistributionViewerCertificateArgs(
        cloudfront_default_certificate=False,
        ssl_support_method="sni-only",
        acm_certificate_arn=global_certificate.arn,
    ),
    tags={"Name": SERVICE_NAME},
    opts=pulumi.ResourceOptions(
        parent=function, depends_on=[global_certificate_validation]
    ),
)

aws.route53.Record(
    resource_name=SERVICE_NAME,
    name=ADMIN_DOMAIN,
    type="A",
    aliases=[
        aws.route53.RecordAliasArgs(
            name=distribution.domain_name,
            zone_id=distribution.hosted_zone_id,
            evaluate_target_health=True,
        )
    ],
    zone_id=zone.id,
    opts=pulumi.ResourceOptions(parent=distribution),
)

# Exports

pulumi.export(f"{SERVICE_NAME}:url", f"https://{ADMIN_DOMAIN}/graphql")
