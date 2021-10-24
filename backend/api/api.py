from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from backend.api.endpoints import items
from backend.utils import ok_status

app = FastAPI()
app.include_router(items.router)


@app.get("/")
async def root():
    # return {"message": "Hello Bigger Applications!"}

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=ok_status
    )
