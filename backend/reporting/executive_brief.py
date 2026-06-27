def generate_executive_brief(
    rankings,
    growth,
    trends,
    themes
):

    if not rankings:

        return (
            "No intelligence available."
        )

    top = rankings[0]

    report = []

    report.append(
        "Atlas Executive Intelligence Brief"
    )

    report.append("")

    report.append(
        f"The knowledge graph currently contains "
        f"{len(rankings)} tracked entities."
    )

    report.append(
        f"The most influential organization is "
        f"{top['entity']} "
        f"(Influence Score: {top['influence_score']})."
    )

    if themes:

        report.append(
            f"The dominant technology theme is "
            f"{themes[0]['theme']} "
            f"with {themes[0]['score']} total mentions."
        )

    if growth:

        report.append(
            f"{len(growth)} entities have recorded "
            f"measurable growth."
        )

    if trends:

        report.append(
            f"{len(trends)} significant trend signals "
            f"were detected."
        )

    else:

        report.append(
            "Historical trend analysis is building its "
            "baseline."
        )

    return "\n".join(report)