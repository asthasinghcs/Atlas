from fastapi import FastAPI

app = FastAPI(
    title="Atlas",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "project": "Atlas",
        "status": "running"
    }