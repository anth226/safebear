# flake8: noqa
import pulumi

stack = pulumi.get_stack()

if stack == "prod":
    from src.dns import google, vercel, wordpress
else:
    from src import inference, vpc
    from src.api import admin, app
