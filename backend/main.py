from fastapi import FastAPI

from api.documents import router as document_router
from api.entities import router as entity_router
from api.graph import router as graph_router
from api.search import router as search_router
from api.entity_documents import router as entity_documents_router
from api.analytics import router as analytics_router
from api.document_entities import router as document_entities_router
from api.related_entities import router as related_entities_router

app = FastAPI(
    title="Atlas"
)

app.include_router(document_router)
app.include_router(entity_router)
app.include_router(graph_router)
app.include_router(search_router)
app.include_router(entity_documents_router)
app.include_router(analytics_router)
app.include_router(document_entities_router)
app.include_router(related_entities_router)


@app.get("/")
def root():
    return {
        "message": "Atlas API running"
    }