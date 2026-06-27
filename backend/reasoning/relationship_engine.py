from models.entity import Entity


def get_related_entities(
    db,
    entity_name
):

    entity = (
        db.query(Entity)
        .filter(
            Entity.name.ilike(entity_name)
        )
        .first()
    )

    if entity is None:
        return []

    related = set()

    for link in entity.document_links:

        document = link.document

        for other_link in document.entity_links:

            if (
                other_link.entity.name
                != entity.name
            ):
                related.add(
                    other_link.entity.name
                )

    return list(related)