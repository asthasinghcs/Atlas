from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db

from models.entity import Entity


router = APIRouter(
    prefix="/entity-documents",
    tags=["Entity Documents"]
)


@router.get("/{entity_name}")
def get_entity_documents(
    entity_name: str,
    db: Session = Depends(get_db)
):

    entity = (
        db.query(Entity)
        .filter(
            Entity.name.ilike(entity_name)
        )
        .first()
    )

    if entity is None:
        return {
            "error": "Entity not found"
        }

    return {
        "entity": entity.name,
        "documents": [
            {
                "id": link.document.id,
                "title": link.document.title
            }
            for link in entity.document_links
        ]
    }