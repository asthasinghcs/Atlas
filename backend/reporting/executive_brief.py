def generate_executive_brief(
    entities
):

    report = []

    report.append(
        "Atlas Executive Intelligence Brief\n"
    )

    for entity in entities[:5]:

        report.append(
            f"- {entity['entity']} "
            f"(Score: "
            f"{entity['influence_score']})"
        )

    return "\n".join(report)