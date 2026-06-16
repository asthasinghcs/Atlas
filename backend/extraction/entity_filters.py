INVALID_ENTITIES = {

    "Premium",
    "Run",
    "Overall",
    "Reviews",
    "Guarantees",
    "Pros",
    "Cons",
    "Team Plan",
    "Position Tracking",
    "White Label",
    "Personalize Personalize",
    "Send",
    "Finds",
    "Limited"
}


def is_valid_entity(
    entity_name: str
):

    if len(entity_name) < 3:
        return False

    if entity_name in INVALID_ENTITIES:
        return False

    return True