from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from db.dependencies import get_db

from models.entity import Entity
from models.document_entity import DocumentEntity

from reporting.trend_classifier import (
    classify_trend
)


router = APIRouter(
    prefix="/trends",
    tags=["Trends"]
)


@router.get("/")
def entity_trends(
    db: Session = Depends(get_db)
):

    results = (
        db.query(
            Entity.name,
            func.count(
                DocumentEntity.id
            ).label("mentions")
        )
        .join(
            DocumentEntity,
            Entity.id == DocumentEntity.entity_id
        )
        .group_by(
            Entity.id
        )
        .order_by(
            func.count(
                DocumentEntity.id
            ).desc()
        )
        .all()
    )

    return [
        {
            "entity": row.name,
            "mentions": row.mentions,
            "trend": classify_trend(
                row.mentions
            )
        }
        for row in results
    ]