import dotenv, pprint
from pydantic import BaseSettings


class Settings(BaseSettings):
    HTTP_HOST: str
    HTTP_PORT: int

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str

    class Config:
        env_file = dotenv.find_dotenv(filename='.env')
        case_sensitive = True


settings = Settings()
pprint.pprint(settings.dict())
