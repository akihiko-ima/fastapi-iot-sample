import os
import sys
import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from routers import auth, comment

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # 許可するドメインを設定
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """処理時間計測"""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.include_router(auth.router)
app.include_router(comment.router)
