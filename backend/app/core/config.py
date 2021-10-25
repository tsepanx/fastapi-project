import dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    REDIS_HOST: str
    REDIS_PASSWORD: str

    class Config:
        env_file = dotenv.find_dotenv(filename='.env')
        case_sensitive = True


settings = Settings()
print(settings.dict())
