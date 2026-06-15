from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db
from models.entity import Entity


router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.get("/entities")
def search_entities(
    q: str,
    db: Session = Depends(get_db)
):

    entities = (
        db.query(Entity)
        .filter(
            Entity.name.ilike(f"%{q}%")
        )
        .all()
    )

    return entities