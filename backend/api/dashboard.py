from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db

from reporting.entity_intelligence import build_entity_intelligence

from reporting.insight_generator import generate_insights

from reporting.executive_brief import generate_executive_brief

from reporting.dashboard_builder import build_dashboard

from reporting.growth_detector import detect_growth

from reporting.theme_detector import detect_themes

from trend_engine.trend_detector import detect_trends


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def dashboard(
    db: Session = Depends(get_db)
):

    rankings = build_entity_intelligence(db)

    top_entities = rankings[:10]

    growth = detect_growth(db)

    themes = detect_themes(db)

    try:

        trends = detect_trends(
            db,
            date.today()
        )

    except Exception:

        trends = []

    insights = generate_insights(
        rankings,
        growth,
        trends,
        themes
    )

    executive_brief = generate_executive_brief(
        rankings,
        growth,
        trends,
        themes
    )

    return build_dashboard(
        db=db,
        top_entities=top_entities,
        insights=insights,
        executive_brief=executive_brief,
        growth=growth,
        trends=trends,
        themes=themes
    )