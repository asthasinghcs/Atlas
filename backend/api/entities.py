from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db
from models.entity import Entity
from schemas.entity_response import EntityResponse

router = APIRouter(
    prefix="/entities",
    tags=["Entities"]
)


@router.get("/", response_model=list[EntityResponse])
def get_entities(
    db: Session = Depends(get_db)
):
    return db.query(Entity).all()