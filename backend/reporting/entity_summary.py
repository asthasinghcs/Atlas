def generate_entity_summary(
    entity_name: str,
    mention_count: int,
    related_entities: list[str]
):

    return (
        f"{entity_name} appears in "
        f"{mention_count} documents. "
        f"Related entities include: "
        f"{', '.join(related_entities)}."
    )