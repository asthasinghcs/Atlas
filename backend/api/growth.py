from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from db.dependencies import get_db

from reporting.growth_detector import (
    detect_growth
)

router = APIRouter(
    prefix="/growth",
    tags=["Growth"]
)


@router.get("/")
def growth(
    db: Session = Depends(get_db)
):

    return detect_growth(db)