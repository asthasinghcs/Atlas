from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from db.dependencies import get_db

from reporting.snapshot_service import (
    capture_snapshot
)


router = APIRouter(
    prefix="/snapshot",
    tags=["Snapshots"]
)


@router.post("/")
def create_snapshot(
    db: Session = Depends(get_db)
):

    capture_snapshot(db)

    return {
        "message":
            "Snapshot captured"
    }