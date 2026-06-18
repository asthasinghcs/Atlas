from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db
from reporting.graph_builder import build_knowledge_graph

router = APIRouter(
    prefix="/knowledge-graph",
    tags=["Knowledge Graph"]
)


@router.get("/")
def knowledge_graph(
    db: Session = Depends(get_db)
):
    return build_knowledge_graph(db)