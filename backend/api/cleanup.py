from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from db.dependencies import get_db

from reporting.entity_cleanup import (
    cleanup_entities
)

router = APIRouter(
    prefix="/cleanup",
    tags=["Cleanup"]
)


@router.post("/")
def cleanup(
    db: Session = Depends(get_db)
):

    removed = cleanup_entities(
        db
    )

    return {
        "removed": removed
    }