from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "mysql+aiomysql://root:110806le@localhost:3306/faculdade_projetoapi"
    DBBaseModel: ClassVar = declarative_base()

    JWT_SECRET: str = "ftmPdYpMIH8tmkbrRZ7kMet_yTsSE7NOE6XoxDBSD-8"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True

settings: Settings = Settings()