def generate_daily_brief(
    entities
):

    report = []

    report.append(
        "Top Intelligence Report\n"
    )

    for idx, entity in enumerate(
        entities,
        start=1
    ):

        report.append(
            f"{idx}. "
            f"{entity['entity']}\n"
            f"   Mentions: "
            f"{entity['mentions']}\n"
            f"   Importance: "
            f"{entity['importance']}\n"
        )

    return "\n".join(report)