def calculate_entity_score(
    mention_count: int
):

    if mention_count >= 20:
        return "Very High"

    if mention_count >= 10:
        return "High"

    if mention_count >= 5:
        return "Medium"

    return "Low"