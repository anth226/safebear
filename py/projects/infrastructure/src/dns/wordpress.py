"""
DNS records for WordPress.com

https://wordpress.com/domains/mapping/safebear.app/setup/safebear.ai?firstVisit=true
https://safebearapp.wordpress.com/
"""


import pulumi
import pulumi_aws as aws

from .domains import SHOWCASE_DOMAIN
from .zone import zone

aws.route53.Record(
    resource_name="wordpress",
    name=SHOWCASE_DOMAIN,
    type="A",
    records=[
        "192.0.78.24",
        "192.0.78.25",
    ],
    ttl=60 * 5,
    zone_id=zone.id,
    opts=pulumi.ResourceOptions(parent=zone),
)

aws.route53.Record(
    resource_name="wordpress-www",
    name=f"www.{SHOWCASE_DOMAIN}",
    type="CNAME",
    records=[SHOWCASE_DOMAIN],
    ttl=60 * 5,
    zone_id=zone.id,
    opts=pulumi.ResourceOptions(parent=zone),
)

aws.route53.Record(
    resource_name="wordpress-verification",
    name=f"wp-domain-ownership-verification.{SHOWCASE_DOMAIN}",
    type="TXT",
    records=["3eac9d33271d5b70a7d668e907ce49e74fada000755f96bda935af90b60dce7f"],
    ttl=60 * 5,
    zone_id=zone.id,
    opts=pulumi.ResourceOptions(parent=zone),
)

pulumi.export("wordpress:url", f"https://{SHOWCASE_DOMAIN}")
