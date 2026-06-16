def generate_insights(
    rankings
):

    insights = []

    if not rankings:
        return insights

    leader = rankings[0]

    insights.append(
        f"{leader['entity']} is currently "
        f"the most influential entity "
        f"in the knowledge graph."
    )

    if len(rankings) >= 3:

        insights.append(
            f"The leading cluster includes "
            f"{rankings[0]['entity']}, "
            f"{rankings[1]['entity']} "
            f"and {rankings[2]['entity']}."
        )

    return insights