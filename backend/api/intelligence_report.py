from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db

from models.entity import Entity
from models.document_entity import DocumentEntity

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

    influence = calculate_influence(
        entity.name,
        mentions,
        db
    )

    relationships = discover_relationships(
        entity.name,
        db
    )

    entity_data = {

        "entity":
            entity.name,

        "entity_type":
            entity.entity_type,

        "mentions":
            mentions,

        "relationship_strength":
            influence[
                "relationship_strength"
            ],

        "unique_connections":
            influence[
                "unique_connections"
            ],

        "influence_score":
            influence[
                "influence_score"
            ],

        "top_connections":
            relationships
    }

    return generate_entity_report(
        entity_data
    )