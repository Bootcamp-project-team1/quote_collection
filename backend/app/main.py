from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from .database import init_db
from .routers import auth

app = FastAPI(title="Quote Collection API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()
app.include_router(auth.router)

@app.get("/")
def root():
    return {"API": "Quote Collection"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="localhost", port=8081, reload=True)
