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

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # frontend IP 로 추후 바꾸기
    allow_credentials=True,
    allow_methods=["*"],  # 모든 method 허용
    allow_headers=["*"],  # 모든 header 허용
)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8081, reload=True)
