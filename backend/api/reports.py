from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from db.dependencies import get_db

from models.entity import Entity
from models.document_entity import DocumentEntity

from reporting.entity_scoring import (
    calculate_entity_score
)


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/top-entities")
def top_entity_report(
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
        .limit(10)
        .all()
    )

    report = []

    for row in results:

        report.append(
            {
                "entity": row.name,
                "mentions": row.mentions,
                "importance": (
                    calculate_entity_score(
                        row.mentions
                    )
                )
            }
        )

    return report