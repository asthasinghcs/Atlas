from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from db.dependencies import get_db

from models.entity import Entity
from models.document_entity import DocumentEntity


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/top-entities")
def top_entities(
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

    return [
        {
            "name": row.name,
            "mentions": row.mentions
        }
        for row in results
    ]