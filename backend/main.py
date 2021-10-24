import uvicorn

from api.api import app
from api.endpoints.items import redis_manager

if __name__ == "__main__":
    print(redis_manager.list_keys())
    uvicorn.run(app, host="0.0.0.0", port=8001)
