from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db

from models.entity import Entity


router = APIRouter(
    prefix="/related-entities",
    tags=["Related Entities"]
)


@router.get("/{entity_name}")
def get_related_entities(
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

    related = set()

    for link in entity.document_links:

        document = link.document

        for other_link in document.entity_links:

            if other_link.entity.name != entity.name:
                related.add(
                    other_link.entity.name
                )

    return {
        "entity": entity.name,
        "related_entities": list(related)
    }