import uvicorn

from api.api import app
from api.endpoints.items import redis_manager

# import sys, os
# sys.path.insert(0, os.path.abspath('..'))

if __name__ == "__main__":
    print(redis_manager.list_keys())
    uvicorn.run(app, host="0.0.0.0", port=8001)
