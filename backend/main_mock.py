import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# 현재 디렉토리를 Python path에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Mock 라우터 import (데이터베이스 없는 실험용)
from app.routers import auth_mock

# FastAPI 앱 생성
app = FastAPI(
    title="API 확인용 mock 버전",
    version="1.0.0",
    description="데이터베이스 없이 API 구조 테스트용",
)

# CORS 설정 (프론트엔드와 통신용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 테스트용으로 모든 오리진 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(auth_mock.router)


@app.get("/")
def root():
    return {
        "note": "이 버전은 메모리에 데이터를 저장 서버를 재시작하면 데이터가 사라짐."
    }


@app.get("/health")
def health_check():
    return {"status": "healthy", "mode": "mock", "database": "in-memory"}


if __name__ == "__main__":
    uvicorn.run("main_mock:app", host="localhost", port=8081, reload=True)
