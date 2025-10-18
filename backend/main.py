from fastapi import FastAPI
from app.routers import router as api_router
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import uvicorn
from contextlib import asynccontextmanager
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database if it doesn't exist
    engine = create_engine(settings.sync_database_url)
    if not database_exists(engine.url):
        create_database(engine.url)

    # Run alembic migrations
    subprocess.run(["alembic", "upgrade", "head"])
    yield

app = FastAPI(lifespan=lifespan)

# # CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # frontend IP 로 추후 바꾸기
#     allow_credentials=True,
#     allow_methods=["*"],  # 모든 method 허용
#     allow_headers=["*"],  # 모든 header 허용
# )

# ----------------- ▼ CORS 설정 수정 ▼ -----------------

# 허용할 출처(origin) 목록을 명시적으로 작성합니다.
origins = [
    "http://localhost:5173",  # React 개발 서버 주소
    "null"                    # 로컬에서 직접 연 html 파일 (test.html)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # ["*"] 대신 위에서 만든 origins 리스트를 사용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------- ▲ CORS 설정 수정 ▲ -----------------


# app.include_router(api_router)

# 모든 API의 시작 경로를 /api로 설정하여 api_router를 등록합니다.
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8081, reload=True)
