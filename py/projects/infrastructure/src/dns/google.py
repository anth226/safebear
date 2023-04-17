import pulumi
import pulumi_aws as aws

from .zone import BASE_DOMAIN, zone

# Google Workspace

# Google Admin Toolbox
# https://toolbox.googleapps.com/apps/checkmx/check?domain=nuage.studio&dkim_selector=

aws.route53.Record(
    resource_name="google-workspace-mx",
    type="MX",
    name=BASE_DOMAIN,
    records=[
        "1 ASPMX.L.GOOGLE.COM",
        "5 ALT1.ASPMX.L.GOOGLE.COM",
        "5 ALT2.ASPMX.L.GOOGLE.COM",
        "10 ALT3.ASPMX.L.GOOGLE.COM",
        "10 ALT4.ASPMX.L.GOOGLE.COM",
    ],
    ttl=60 * 60 * 24,
    zone_id=zone.id,
    opts=pulumi.ResourceOptions(parent=zone, protect=True),
)

# https://support.google.com/a/answer/10683907?hl=en&ref_topic=10685331
aws.route53.Record(
    resource_name="google-workspace-spf",
    type="TXT",
    name="@",
    records=["v=spf1 include:_spf.google.com ~all"],
    ttl=5 * 60,
    zone_id=zone.id,
    opts=pulumi.ResourceOptions(parent=zone),
)

# https://support.google.com/a/answer/174126
dkim_value = (
    "v=DKIM1; "
    "k=rsa; "
    "p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCT19qPn5HDmlCg2WR1/1H+y5BCHI+eLyG6qSxpJXmZ"
    "2runCrmqm2RBU1+Mxk+ZU26gxfEFgD6tFTjpgYVqRdFE5n/LjaAS8k0vgqFDjafNua23+FRX6F92QopIBc"
    "PdkZTob6VwCwPk3RD/vA3QqPmEOtYWAR6DJnxs96hxEmAkCwIDAQAB"
)
dkim_record = aws.route53.Record(
    resource_name="google-workspace-dkim",
    type="TXT",
    name="google._domainkey",
    records=[dkim_value],
    ttl=5 * 60,
    zone_id=zone.id,
    opts=pulumi.ResourceOptions(parent=zone),
)

# https://support.google.com/a/answer/2466563#dmarc-record-tags
aws.route53.Record(
    resource_name="google-workspace-dmarc",
    type="TXT",
    name=f"_dmarc.{BASE_DOMAIN}",
    records=["v=DMARC1; p=reject;"],
    ttl=5 * 60,
    zone_id=zone.id,
    opts=pulumi.ResourceOptions(
        parent=zone,
        depends_on=[
            # Reject non-compliant emails
            dkim_record
        ],
    ),
)
