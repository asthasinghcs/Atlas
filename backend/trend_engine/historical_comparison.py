from datetime import date
from datetime import timedelta

from sqlalchemy.orm import Session

from models.trend_snapshot import TrendSnapshot


def compare_with_previous_snapshot(
    db: Session,
    snapshot_date: date
):

    previous_date = (
        snapshot_date -
        timedelta(days=1)
    )

    current_snapshots = (
        db.query(TrendSnapshot)
        .filter(
            TrendSnapshot.snapshot_date == snapshot_date
        )
        .all()
    )

    previous_snapshots = (
        db.query(TrendSnapshot)
        .filter(
            TrendSnapshot.snapshot_date == previous_date
        )
        .all()
    )

    previous_lookup = {
        snapshot.entity_name: snapshot
        for snapshot in previous_snapshots
    }

    comparisons = []

    for current in current_snapshots:

        previous = previous_lookup.get(
            current.entity_name
        )

        if previous is None:

            comparisons.append(
                {
                    "entity": current.entity_name,
                    "status": "new",
                    "mention_change": current.mentions,
                    "influence_change": current.influence_score,
                    "relationship_change": current.relationship_count
                }
            )

            continue

        comparisons.append(
            {
                "entity": current.entity_name,
                "status": "existing",

                "mention_change":
                    current.mentions -
                    previous.mentions,

                "influence_change":
                    current.influence_score -
                    previous.influence_score,

                "relationship_change":
                    current.relationship_count -
                    previous.relationship_count
            }
        )

    return comparisons