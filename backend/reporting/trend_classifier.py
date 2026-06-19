def classify_trend(
    mention_count: int
):

    if mention_count >= 10:
        return "Trending"

    if mention_count >= 5:
        return "Emerging"

    return "Low Activity"