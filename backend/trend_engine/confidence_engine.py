def calculate_confidence(
    article_count: int,
    source_count: int,
    relationship_count: int,
    mention_change: int
):

    score = 0

    # Evidence

    score += min(
        article_count * 2,
        30
    )

    # Source diversity

    score += min(
        source_count * 4,
        25
    )

    # Graph connectivity

    score += min(
        relationship_count,
        20
    )

    # Momentum

    score += min(
        abs(mention_change),
        15
    )

    confidence = min(
        score,
        100
    )

    if confidence >= 85:
        level = "Very High"

    elif confidence >= 70:
        level = "High"

    elif confidence >= 50:
        level = "Medium"

    else:
        level = "Low"

    return {
        "confidence_score": confidence,
        "confidence_level": level
    }