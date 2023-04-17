import pulumi
import pulumi_aws as aws

from .dns.domains import STACK_DOMAIN
from .dns.zone import zone

aws_config = pulumi.Config("aws")

global_provider = aws.Provider(
    resource_name="global",
    region="us-east-1",
    profile=aws_config.require("profile"),
    allowed_account_ids=aws_config.require_object("allowedAccountIds"),
    default_tags=aws_config.require_object("defaultTags"),
)

global_certificate = aws.acm.Certificate(
    resource_name="global",
    domain_name=STACK_DOMAIN,
    subject_alternative_names=[f"*.{STACK_DOMAIN}"],
    validation_method="DNS",
    opts=pulumi.ResourceOptions(provider=global_provider),
)

regional_certificate = aws.acm.Certificate(
    resource_name="regional",
    domain_name=STACK_DOMAIN,
    subject_alternative_names=[f"*.{STACK_DOMAIN}"],
    validation_method="DNS",
)

# Note: global & regional share the same validation records
validation_records = regional_certificate.domain_validation_options.apply(
    lambda dvos: [
        aws.route53.Record(
            resource_name=f"validation-{i+1}",
            name=dvo.resource_record_name,
            type=dvo.resource_record_type,
            zone_id=zone.zone_id,
            records=[dvo.resource_record_value],  # type: ignore
            ttl=300,
            # APEX & wildcard share the same validation record,
            # so we need to allow overwrite to avoid duplicates
            allow_overwrite=True,
            opts=pulumi.ResourceOptions(delete_before_replace=True),
        )
        for i, dvo in enumerate(dvos)
    ]
)

regional_certificate_validation = aws.acm.CertificateValidation(
    resource_name="regional",
    certificate_arn=regional_certificate.arn,
    validation_record_fqdns=validation_records.apply(
        lambda records: [record.fqdn for record in records]
    ),
    opts=pulumi.ResourceOptions(
        parent=regional_certificate, depends_on=validation_records
    ),
)

global_certificate_validation = aws.acm.CertificateValidation(
    resource_name="global",
    certificate_arn=global_certificate.arn,
    validation_record_fqdns=validation_records.apply(
        lambda records: [record.fqdn for record in records]
    ),
    opts=pulumi.ResourceOptions(
        parent=global_certificate, depends_on=validation_records
    ),
)
