import secrets

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "telex-jotform"
    PROJECT_VERSION: str = "0.0.1"
    PROJECT_DESCRIPTION: str = "telex jotform integration"
    API_PREFIX: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DEBUG: bool = False
    TESTING: bool = False
    TELEX_WEBHOOK: str = "https://ping.telex.im/v1/webhooks"
    

settings = Settings()
