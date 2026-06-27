from sqlalchemy import func

from models.document import Document
from models.document_entity import DocumentEntity
from models.entity import Entity


def build_dashboard(
    db,
    top_entities,
    insights,
    executive_brief,
    growth,
    trends,
    themes
):

    entity_count = (
        db.query(Entity)
        .count()
    )

    document_count = (
        db.query(Document)
        .count()
    )

    relationship_count = (
        db.query(DocumentEntity)
        .count()
    )

    average_influence = 0

    if top_entities:

        average_influence = int(
            sum(
                entity["influence_score"]
                for entity in top_entities
            )
            / len(top_entities)
        )

    return {

        "top_entities": top_entities,

        "executive_brief": executive_brief,

        "insights": insights,

        "growth": growth[:10],

        "trends": trends[:10],

        "themes": themes[:10],

        "stats": {

            "entities": entity_count,

            "relationships": relationship_count,

            "documents": document_count,

            "average_influence": average_influence

        }

    }