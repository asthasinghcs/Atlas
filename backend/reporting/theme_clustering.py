from collections import defaultdict

from sqlalchemy.orm import Session

from models.entity import Entity

from reasoning.relationship_engine import get_related_entities


def discover_themes(
    db: Session
):

    themes = []

    entities = (
        db.query(Entity)
        .all()
    )

    visited = set()

    for entity in entities:

        if entity.name in visited:
            continue

        related = get_related_entities(
            db,
            entity.name
        )

        cluster = [
            entity.name
        ]

        for item in related[:5]:

            cluster.append(item)

        cluster = list(
            set(cluster)
        )

        if len(cluster) < 3:
            continue

        for item in cluster:
            visited.add(item)

        themes.append(
            {
                "theme_seed": entity.name,
                "entities": cluster,
                "size": len(cluster)
            }
        )

    themes.sort(
        key=lambda x: x["size"],
        reverse=True
    )

    return themes[:10]