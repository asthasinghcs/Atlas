from datetime import date

from sqlalchemy.orm import Session

from models.entity import Entity
from models.trend_snapshot import TrendSnapshot

from reporting.influence import calculate_influence
from reporting.relationship_discovery import discover_relationships


def build_daily_snapshot(
    db: Session
):

    today = date.today()
    
    existing = (
    db.query(TrendSnapshot)
    .filter(
        TrendSnapshot.snapshot_date == today
    )
    .first()
    )

    if existing:

        return {
            "snapshot_date": today,
            "entities_saved": 0
        }

    entities = db.query(Entity).all()

    snapshots_created = 0

    for entity in entities:

        mentions = len(
            entity.document_links
        )

        relationships = discover_relationships(
            entity.name,
            db
        )

        influence = calculate_influence(
            entity.name,
            mentions,
            db
        )

        snapshot = TrendSnapshot(

            snapshot_date=today,

            entity_name=entity.name,

            entity_type=entity.entity_type,

            mentions=mentions,

            influence_score=(
                influence["influence_score"]
            ),

            relationship_count=len(
                relationships
            ),

            theme=None
        )

        db.add(snapshot)

        snapshots_created += 1

    db.commit()

    return {
        "snapshot_date": today,
        "entities_saved": snapshots_created
    }