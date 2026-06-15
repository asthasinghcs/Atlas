from fastapi import FastAPI

from api.documents import router as document_router
from api.entities import router as entity_router

app = FastAPI(
    title="Atlas",
    version="1.0.0"
)

app.include_router(document_router)
app.include_router(entity_router)

@app.get("/")
def root():
    return {
        "project": "Atlas",
        "status": "running"
    }