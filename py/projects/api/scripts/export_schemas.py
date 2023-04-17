from pathlib import Path

from src.admin.schema import schema as admin_schema
from src.app.schema import schema as app_schema

monorepo_root = Path(__file__).parents[4]

app_schema_path = monorepo_root / "app.graphql"
admin_schema_path = monorepo_root / "admin.graphql"

app_schema_path.write_text(app_schema.as_str())
print(f"Wrote {app_schema_path}")

admin_schema_path.write_text(admin_schema.as_str())
print(f"Wrote {admin_schema_path}")
