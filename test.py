from fastapi import FastAPI
from starlette.responses import FileResponse
from starlette.requests import Request
from starlette.middleware.cors import CORSMiddleware
import time

app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

@app.get('/')
async def hello():
    time.sleep(5)  # Sleeps for 5 seconds
    return {"Hello": "World"}


@app.get("/keep_warm")
async def keep_warm():
    return "ok"