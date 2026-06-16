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

from reporting.executive_brief import (
    generate_executive_brief
)


router = APIRouter(
    prefix="/executive-brief",
    tags=["Executive Brief"]
)


@router.get("/")
def executive_brief(
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
                "influence_score":
                    influence[
                        "influence_score"
                    ]
            }
        )

    rankings.sort(
        key=lambda x:
            x["influence_score"],
        reverse=True
    )

    return {
        "brief":
            generate_executive_brief(
                rankings
            )
    }