import os
import secrets
from socket import SIO_LOOPBACK_FAST_PATH

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "telex-jotform"
    PROJECT_VERSION: str = "0.0.1"
    PROJECT_DESCRIPTION: str = "telex jotform integration"
    API_PREFIX: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DEBUG: bool = False
    TESTING: bool = False

settings = Settings()
