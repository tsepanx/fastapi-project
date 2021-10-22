import uvicorn
from api import app, redis_manager


if __name__ == "__main__":
    print(redis_manager.list_keys())
    uvicorn.run(app, host="0.0.0.0", port=8001)
