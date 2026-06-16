from models.entity_metric import (
    EntityMetric
)


def detect_growth(db):

    entities = (
        db.query(
            EntityMetric.entity_name
        )
        .distinct()
        .all()
    )

    growth_report = []

    for entity_tuple in entities:

        entity_name = entity_tuple[0]

        snapshots = (
            db.query(EntityMetric)
            .filter(
                EntityMetric.entity_name
                == entity_name
            )
            .order_by(
                EntityMetric.captured_at.desc()
            )
            .limit(2)
            .all()
        )

        if len(snapshots) < 2:
            continue

        latest = snapshots[0]
        previous = snapshots[1]

        old_score = (
            previous.influence_score
        )

        new_score = (
            latest.influence_score
        )

        growth = (
            new_score - old_score
        )

        growth_report.append(
            {
                "entity": entity_name,
                "old_score": old_score,
                "new_score": new_score,
                "growth": growth
            }
        )

    growth_report.sort(
        key=lambda x: x["growth"],
        reverse=True
    )

    return growth_report[:20]