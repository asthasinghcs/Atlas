from reporting.relationship_discovery import (
    discover_relationships
)


def calculate_influence(
    entity_name: str,
    mentions: int,
    db
):

    relationships = discover_relationships(
        entity_name,
        db
    )

    total_strength = sum(
        relation["co_occurrences"]
        for relation in relationships
    )

    unique_connections = len(
        relationships
    )

    influence_score = (
        mentions * 2
        + total_strength * 3
        + unique_connections * 5
    )

    return {
        "mentions": mentions,
        "unique_connections": unique_connections,
        "relationship_strength": total_strength,
        "influence_score": influence_score
    }