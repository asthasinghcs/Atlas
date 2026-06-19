from sqlalchemy.orm import Session

from models.entity import Entity
from models.document_entity import DocumentEntity

from reporting.influence import (
    calculate_influence
)

from reporting.relationship_discovery import (
    discover_relationships
)


def build_entity_intelligence(
    db: Session
):

    rankings = []

    entities = (
        db.query(Entity)
        .all()
    )

    for entity in entities:

        mentions = (
            db.query(DocumentEntity)
            .filter(
                DocumentEntity.entity_id
                == entity.id
            )
            .count()
        )

        influence = calculate_influence(
            entity.name,
            mentions,
            db
        )

        relationships = discover_relationships(
            entity.name,
            db
        )

        rankings.append(
            {
                "entity":
                    entity.name,

                "entity_type":
                    entity.entity_type,

                "mentions":
                    mentions,

                "relationship_strength":
                    influence[
                        "relationship_strength"
                    ],

                "unique_connections":
                    influence[
                        "unique_connections"
                    ],

                "influence_score":
                    influence[
                        "influence_score"
                    ],

                "top_connections":
                    relationships
            }
        )

    rankings.sort(
        key=lambda x:
            x["influence_score"],
        reverse=True
    )

    return rankings