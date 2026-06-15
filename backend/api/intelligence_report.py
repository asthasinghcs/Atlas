from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db

from models.entity import Entity
from models.document_entity import (
    DocumentEntity
)

from reporting.relationship_discovery import (
    discover_relationships
)

from reporting.influence import (
    calculate_influence
)

from reporting.intelligence_engine import (
    generate_entity_report
)


router = APIRouter(
    prefix="/intelligence-report",
    tags=["Intelligence Report"]
)


@router.get("/{entity_name}")
def intelligence_report(
    entity_name: str,
    db: Session = Depends(get_db)
):

    entity = (
        db.query(Entity)
        .filter(
            Entity.name == entity_name
        )
        .first()
    )

    if entity is None:
        return {
            "error": "Entity not found"
        }

    mentions = (
        db.query(DocumentEntity)
        .filter(
            DocumentEntity.entity_id
            == entity.id
        )
        .count()
    )

    influence = (
        calculate_influence(
            entity.name,
            mentions,
            db
        )
    )

    relationships = (
        discover_relationships(
            entity.name,
            db
        )
    )

    return generate_entity_report(
        entity.name,
        mentions,
        influence[
            "relationship_strength"
        ],
        influence[
            "influence_score"
        ],
        relationships
    )