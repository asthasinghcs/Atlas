from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db

from reporting.entity_intelligence import (
    build_entity_intelligence
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

    rankings = build_entity_intelligence(
        db
    )

    top_entities = rankings[:5]

    insights = generate_insights(
        rankings
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