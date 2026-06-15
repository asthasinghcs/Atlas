from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db
from models.entity import Entity

from reporting.entity_summary import (
    generate_entity_summary
)


router = APIRouter(
    prefix="/intelligence",
    tags=["Intelligence"]
)


@router.get("/entity/{entity_name}")
def entity_intelligence(
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

    summary = generate_entity_summary(
        entity_name=entity.name,
        mention_count=len(
            entity.document_links
        ),
        related_entities=list(
            related_entities
        )
    )

    return {
        "entity": entity.name,
        "summary": summary
    }