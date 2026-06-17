from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db

from models.entity import Entity

from reasoning.relationship_engine import get_related_entities


router = APIRouter(
    prefix="/related-entities",
    tags=["Related Entities"]
)


@router.get("/{entity_name}")
def related_entities(
    entity_name: str,
    db: Session = Depends(get_db)
):

    return {
        "entity": entity_name,
        "related_entities":
            get_related_entities(
                entity_name,
                db
            )
    }