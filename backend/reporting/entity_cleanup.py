from models.entity import Entity


BAD_TERMS = {
    "Premium",
    "Run",
    "Overall",
    "Reviews",
    "Guarantees",
    "Pros",
    "Cons",
    "Send",
    "Finds"
}


def cleanup_entities(db):

    entities = (
        db.query(Entity)
        .all()
    )

    removed = 0

    for entity in entities:

        if entity.name in BAD_TERMS:

            db.delete(entity)

            removed += 1

    db.commit()

    return removed