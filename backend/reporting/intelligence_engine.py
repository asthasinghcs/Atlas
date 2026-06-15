def classify_entity(
    influence_score: int
):

    if influence_score >= 30:
        return "Highly Influential"

    if influence_score >= 20:
        return "Influential"

    if influence_score >= 10:
        return "Emerging"

    return "Low Impact"


def generate_entity_report(
    entity_name: str,
    mentions: int,
    relationship_strength: int,
    influence_score: int,
    top_connections: list
):

    classification = classify_entity(
        influence_score
    )

    connection_names = [
        connection["name"]
        for connection in top_connections[:3]
    ]

    summary = (
        f"{entity_name} is a "
        f"{classification.lower()} entity "
        f"within the Atlas knowledge graph. "
        f"It appears in {mentions} documents "
        f"and has a relationship strength of "
        f"{relationship_strength}. "
        f"Strong connections include "
        f"{', '.join(connection_names)}."
    )

    return {
        "entity": entity_name,
        "classification": classification,
        "mentions": mentions,
        "relationship_strength":
            relationship_strength,
        "influence_score":
            influence_score,
        "summary": summary
    }