from pydantic import BaseSettings
import logging


class Settings(BaseSettings):
    app_name: str = "Correlations website API"
    admin_email: str = "mtokat1@gmail.com"
    LOG_FORMAT = "%(levelname)s %(filename)s line:%(lineno)d %(asctime)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


class TestSettings(Settings):
    DYNAMODB_TABLE: str = "correlations"
    CORS_WHITELIST = [
        "http://localhost:3000",
    ]


class ProdSettings(Settings):
    DYNAMODB_TABLE: str = "correlations"
    CORS_WHITELIST = [
        "http://mywebsite.com",
    ]


# Set it TestSettings() or ProdSettings()
settings = TestSettings()
