from fastapi import FastAPI

from api.documents import router as document_router
from api.entities import router as entity_router
from api.graph import router as graph_router
from api.search import router as search_router
from api.entity_documents import router as entity_documents_router
from api.analytics import router as analytics_router
from api.document_entities import router as document_entities_router
from api.related_entities import router as related_entities_router
from api.entity_profile import router as entity_profile_router
from api.intelligence import router as intelligence_router
from api.scoring import router as scoring_router
from api.reports import router as reports_router
from api.daily_brief import router as daily_brief_router
from api.trends import router as trends_router
from api.relationships import (
    router as relationships_router
)
from api.network import (
    router as network_router
)
from api.influence import (
    router as influence_router
)

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
app.include_router(entity_profile_router)
app.include_router(intelligence_router)
app.include_router(scoring_router)
app.include_router(reports_router)
app.include_router(daily_brief_router)
app.include_router(trends_router)
app.include_router(
    relationships_router
)
app.include_router(
    network_router
)
app.include_router(
    influence_router
)

@app.get("/")
def root():
    return {
        "message": "Atlas API running"
    }