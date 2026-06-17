from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from db.dependencies import get_db

from reporting.theme_clustering import (
    discover_themes
)

router = APIRouter(
    prefix="/discovered-themes",
    tags=["Discovered Themes"]
)


@router.get("/")
def discovered_themes(
    db: Session = Depends(get_db)
):

    return discover_themes(db)