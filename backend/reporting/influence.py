from reporting.relationship_discovery import (
    discover_relationships
)


def calculate_influence(
    entity_name: str,
    mentions: int,
    db
):

    relationships = (
        discover_relationships(
            entity_name,
            db
        )
    )

    total_strength = sum(
        relation["co_occurrences"]
        for relation in relationships
    )

    return {
        "mentions": mentions,
        "relationship_strength":
            total_strength,
        "influence_score":
            mentions +
            total_strength
    }