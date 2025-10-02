from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.routers import auth, tag, book, publisher

# FastAPI 앱 생성
app = FastAPI(title="Quote Collection API", version="1.0.0")

# CORS 설정 (프론트엔드와 통신용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 라우터 등록
app.include_router(auth.router)
app.include_router(tag.router)
app.include_router(book.router)
app.include_router(publisher.router)


@app.get("/")
def root():
    return {"API": "Quote Collection"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8081, reload=True)
