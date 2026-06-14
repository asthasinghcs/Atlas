from fastapi import FastAPI

from api.documents import router as document_router

app = FastAPI(
    title="Atlas",
    version="1.0.0"
)

app.include_router(document_router)


@app.get("/")
def root():
    return {
        "project": "Atlas",
        "status": "running"
    }