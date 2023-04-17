import pulumi
import pulumi_aws as aws

from .domains import ADMIN_DOMAIN, APP_DOMAIN
from .zone import zone

aws.route53.Record(
    resource_name="app",
    name=APP_DOMAIN,
    type="CNAME",
    records=[
        "cname.vercel-dns.com",
        # "76.76.21.21" # for APEX
    ],
    ttl=60 * 60,
    zone_id=zone.id,
    opts=pulumi.ResourceOptions(parent=zone),
)

aws.route53.Record(
    resource_name="admin",
    name=ADMIN_DOMAIN,
    type="CNAME",
    records=[
        "cname.vercel-dns.com",
        # "76.76.21.21" # for APEX
    ],
    ttl=60 * 60,
    zone_id=zone.id,
    opts=pulumi.ResourceOptions(parent=zone),
)
