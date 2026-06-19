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
    entity: dict
):

    classification = classify_entity(
        entity["influence_score"]
    )

    connection_names = [
        connection["name"]
        for connection in entity.get(
            "top_connections",
            []
        )[:3]
    ]

    summary = (
        f"{entity['entity']} is a "
        f"{classification.lower()} entity "
        f"within the Atlas knowledge graph. "
        f"It appears in "
        f"{entity['mentions']} documents "
        f"and has a relationship strength of "
        f"{entity['relationship_strength']}. "
    )

    if connection_names:

        summary += (
            "Strong connections include "
            f"{', '.join(connection_names)}."
        )

    return {

        **entity,

        "classification":
            classification,

        "summary":
            summary
    }