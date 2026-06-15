from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db

from models.entity import Entity
from models.document_entity import DocumentEntity

from reporting.relationship_discovery import (
    discover_relationships
)


router = APIRouter(
    prefix="/influence",
    tags=["Influence"]
)


@router.get("/")
def influence_ranking(
    db: Session = Depends(get_db)
):

    entities = (
        db.query(Entity)
        .all()
    )

    rankings = []

    for entity in entities:

        mentions = (
            db.query(DocumentEntity)
            .filter(
                DocumentEntity.entity_id
                == entity.id
            )
            .count()
        )

        connections = len(
            discover_relationships(
                entity.name,
                db
            )
        )

        influence_score = (
            mentions +
            connections
        )

        rankings.append(
            {
                "entity": entity.name,
                "mentions": mentions,
                "connections": connections,
                "influence_score":
                    influence_score
            }
        )

    rankings.sort(
        key=lambda x:
            x["influence_score"],
        reverse=True
    )

    return rankings[:10]