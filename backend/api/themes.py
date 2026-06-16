from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from db.dependencies import get_db

from reporting.theme_detector import (
    detect_themes
)

router = APIRouter(
    prefix="/themes",
    tags=["Themes"]
)


@router.get("/")
def themes(
    db: Session = Depends(get_db)
):

    return detect_themes(db)