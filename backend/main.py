from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"API": "Quote Collection"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8081, reload=True)
