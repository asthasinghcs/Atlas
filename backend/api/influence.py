from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db

from models.entity import Entity
from models.document_entity import (
    DocumentEntity
)

from reporting.influence import (
    calculate_influence
)


router = APIRouter(
    prefix="/influence",
    tags=["Influence"]
)


@router.get("/")
def influence_ranking(
    db: Session = Depends(get_db)
):

    rankings = []

    entities = (
        db.query(Entity)
        .all()
    )

    for entity in entities:

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

        rankings.append(
            {
                "entity": entity.name,
                **influence
            }
        )

    rankings.sort(
        key=lambda x:
            x["influence_score"],
        reverse=True
    )

    return rankings[:10]