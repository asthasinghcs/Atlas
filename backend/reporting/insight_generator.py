def generate_insights(
    rankings,
    growth,
    trends,
    themes
):

    insights = []

    if rankings:

        leader = rankings[0]

        insights.append(
            f"{leader['entity']} leads the intelligence graph "
            f"with an influence score of "
            f"{leader['influence_score']}."
        )

    if growth:

        fastest = growth[0]

        insights.append(
            f"{fastest['entity']} recorded the strongest "
            f"growth (+{fastest['growth']})."
        )

    if themes:

        dominant = themes[0]

        insights.append(
            f"{dominant['theme']} is currently the dominant "
            f"technology theme "
            f"({dominant['score']} total mentions)."
        )

    if trends:

        top = trends[0]

        insights.append(
            f"{top['entity']} is showing a "
            f"{top['trend'].replace('_', ' ')} trend."
        )

    else:

        insights.append(
            "Historical trend analysis is building its baseline."
        )

    return insights