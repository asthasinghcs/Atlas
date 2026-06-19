from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db

from reporting.entity_intelligence import (
    build_entity_intelligence
)


router = APIRouter(
    prefix="/influence",
    tags=["Influence"]
)


@router.get("/")
def influence_ranking(
    db: Session = Depends(get_db)
):

    rankings = build_entity_intelligence(
        db
    )

    return rankings[:10]