from fastapi import FastAPI

from routers import owo_router


app = FastAPI()

app.include_router(
    owo_router,
    prefix="/owo",
)
