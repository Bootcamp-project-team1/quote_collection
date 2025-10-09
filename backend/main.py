from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.models import user, book, like, producer, publisher, quote_tag, quote, source, tag
from app.routers import auth, book, like, producer, publisher, quote_tag, quote, source, tag
from app.database import Base, engine


def create_tables():
    Base.metadata.create_all(bind=engine)

# FastAPI 앱 생성
app = FastAPI(title="Quote Collection API", version="1.0.0")

@app.on_event("startup")
def on_startup():
    create_tables()

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
app.include_router(like.router)
app.include_router(quote.router)
app.include_router(quote_tag.router)
app.include_router(producer.router)
app.include_router(source.router)





@app.get("/")
def root():
    return {"API": "Quote Collection"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8081, reload=True)
