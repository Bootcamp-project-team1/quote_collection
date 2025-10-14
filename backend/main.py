from fastapi import FastAPI
from app.routers import router as api_router
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import uvicorn

app = FastAPI()

@app.on_event("startup")
def startup_event():
    subprocess.run(["alembic", "upgrade", "head"])

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




