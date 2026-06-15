from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db

from reporting.relationship_discovery import (
    discover_relationships
)

router = APIRouter(
    prefix="/network",
    tags=["Network"]
)


@router.get("/{entity_name}")
def network_report(
    entity_name: str,
    db: Session = Depends(get_db)
):

    relationships = discover_relationships(
        entity_name,
        db
    )

    return {
        "entity": entity_name,
        "connection_count": len(
            relationships
        ),
        "strongest_connections":
            relationships[:5]
    }