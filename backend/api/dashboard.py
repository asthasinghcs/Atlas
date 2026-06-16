from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db

from models.entity import Entity
from models.document_entity import DocumentEntity

from reporting.influence import (
    calculate_influence
)

from reporting.insight_generator import (
    generate_insights
)

from reporting.executive_brief import (
    generate_executive_brief
)

from reporting.dashboard_builder import (
    build_dashboard
)


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def dashboard(
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

    top_entities = rankings[:5]

    insights = (
        generate_insights(
            rankings
        )
    )

    executive_brief = (
        generate_executive_brief(
            rankings
        )
    )

    return build_dashboard(
        top_entities,
        insights,
        executive_brief
    )