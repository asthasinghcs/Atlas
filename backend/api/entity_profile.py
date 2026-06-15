from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db
from models.entity import Entity


router = APIRouter(
    prefix="/entity-profile",
    tags=["Entity Profile"]
)


@router.get("/{entity_name}")
def get_entity_profile(
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

    related_entities = set()

    for link in entity.document_links:

        document = link.document

        for other_link in document.entity_links:

            if other_link.entity.name != entity.name:
                related_entities.add(
                    other_link.entity.name
                )

    return {
        "name": entity.name,
        "entity_type": entity.entity_type,
        "mention_count": len(
            entity.document_links
        ),
        "related_entities": list(
            related_entities
        ),
        "documents": [
            {
                "id": link.document.id,
                "title": link.document.title
            }
            for link in entity.document_links
        ]
    }