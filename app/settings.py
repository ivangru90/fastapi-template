import secrets
from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, validator

class Settings(BaseSettings):
  API_V1_STR: str = "/api/v1"
  MODEL_PATH: str = ""
  SECRET_KEY: str = secrets.token_urlsafe(32)
  ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
  ALGORITHM = "HS256"
  #SERVER_NAME: str
  #SERVER_HOST: AnyHttpUrl

  DB_USERNAME = "macaktom"
  DB_PASSWORD = "volimdzerija"
  DB_SERVER_NAME = "postgres"
  DB_SERVER_PORT = 5432
  DB_NAME = "appdb"
  SSL_MODE: str = "prefer"
  DATABASE_URL = "postgresql://{}:{}@{}:{}/{}?sslmode={}".format(DB_USERNAME, DB_PASSWORD, DB_SERVER_NAME, DB_SERVER_PORT, DB_NAME, SSL_MODE)

  PROJECT_NAME: str = "REST FASTAPI"
  BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:5000","https://localhost:5000"]

  @validator("BACKEND_CORS_ORIGINS", pre=True)
  def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
    if isinstance(v, str) and not v.startswith("["):
      return [i.strip() for i in v.split(",")]
    elif isinstance(v, (list, str)):
      return v
    raise ValueError(v)

settings = Settings()