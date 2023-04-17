from pathlib import Path

from pydantic import BaseModel, BaseSettings, SecretStr

monorepo_root = Path(__file__).parents[4]
local_dotenv = monorepo_root / ".env"


class DatabaseSettings(BaseModel):
    host: str
    port: int
    username: str
    password: SecretStr
    name: str


class FakerSettings(BaseModel):
    enabled: bool = False
    locale: str = "fr_FR"
    seed: int | None = None


class GraphQLSettings(BaseSettings):
    """Settings for the API."""

    debug: bool = False
    powertools_service_name: str | None = None
    faker: FakerSettings = FakerSettings()

    class Config:
        """Config for the Settings."""

        env_file = local_dotenv
        env_file_encoding = "utf-8"


# Create settings instances
app_settings = GraphQLSettings(powertools_service_name="app")
admin_settings = GraphQLSettings(powertools_service_name="admin")
