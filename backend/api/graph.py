from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db

from models.entity import Entity


router = APIRouter(
    prefix="/graph",
    tags=["Graph"]
)


@router.get("/entity/{entity_id}")
def get_entity_graph(
    entity_id: int,
    db: Session = Depends(get_db)
):

    entity = (
        db.query(Entity)
        .filter(Entity.id == entity_id)
        .first()
    )

    if entity is None:
        return {
            "error": "Entity not found"
        }

    return {
        "entity": entity.name,
        "entity_type": entity.entity_type,
        "documents": [
            {
                "id": link.document.id,
                "title": link.document.title
            }
            for link in entity.document_links
        ]
    }