from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db
from models.entity import Entity

from reporting.entity_scoring import (
    calculate_entity_score
)


router = APIRouter(
    prefix="/scoring",
    tags=["Scoring"]
)


@router.get("/entity/{entity_name}")
def score_entity(
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

    mention_count = len(
        entity.document_links
    )

    score = calculate_entity_score(
        mention_count
    )

    return {
        "entity": entity.name,
        "mention_count": mention_count,
        "importance": score
    }