from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db

from reporting.relationship_discovery import (
    discover_relationships
)

router = APIRouter(
    prefix="/relationships",
    tags=["Relationships"]
)


@router.get("/{entity_name}")
def get_relationships(
    entity_name: str,
    db: Session = Depends(get_db)
):

    return {
        "entity": entity_name,
        "related_entities":
            discover_relationships(
                entity_name,
                db
            )
    }