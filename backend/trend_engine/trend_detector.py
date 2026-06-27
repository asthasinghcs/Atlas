from trend_engine.historical_comparison import (
    compare_with_previous_snapshot
)


def detect_trends(
    db,
    snapshot_date
):

    comparisons = compare_with_previous_snapshot(
        db,
        snapshot_date
    )

    trends = []

    for item in comparisons:

        if item["status"] == "new":

            trend = "emerging"

        elif item["mention_change"] >= 10:

            trend = "rapid_growth"

        elif item["mention_change"] >= 3:

            trend = "growing"

        elif item["mention_change"] <= -10:

            trend = "rapid_decline"

        elif item["mention_change"] <= -3:

            trend = "declining"

        else:

            trend = "stable"

        if trend != "stable":

            trends.append(
                {
                    "entity": item["entity"],
                    "trend": trend,
                    "mention_change":
                        item["mention_change"],
                    "influence_change":
                        item["influence_change"],
                    "relationship_change":
                        item["relationship_change"]
                }
            )

    trends.sort(
        key=lambda x: (
            abs(x["mention_change"]),
            abs(x["influence_change"])
        ),
        reverse=True
    )

    return trends