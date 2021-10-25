import uvicorn

from api.api import app
from api.endpoints.items import redis_manager
from app.core.config import settings


# Called only when directly run main.py
if __name__ == "__main__":
    print(redis_manager.list_keys())

    uvicorn.run(
        app,
        host=settings.HTTP_HOST,
        port=settings.HTTP_PORT
    )
