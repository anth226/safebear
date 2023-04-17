import pulumi

BASE_DOMAIN = "safebear.ai"

stack = pulumi.get_stack()
STACK_DOMAIN = BASE_DOMAIN if stack == "prod" else f"{stack}.{BASE_DOMAIN}"

# Showcase website (Wordpress)

SHOWCASE_DOMAIN = STACK_DOMAIN

# API

API_DOMAIN = f"api.{STACK_DOMAIN}"

# App website

APP_DOMAIN = f"app.{STACK_DOMAIN}"

# Admin dashboard

ADMIN_DOMAIN = f"admin.{STACK_DOMAIN}"
