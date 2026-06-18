import re

from config.entity_aliases import ENTITY_ALIASES


def normalize_entity(
    entity_name: str
) -> str:

    if not entity_name:
        return ""

    entity_name = entity_name.strip()

    entity_name = re.sub(
        r"\s+",
        " ",
        entity_name
    )

    entity_name = entity_name.replace(
        "\n",
        " "
    )

    lookup = entity_name.lower()

    if lookup in ENTITY_ALIASES:
        return ENTITY_ALIASES[lookup]

    words = entity_name.split()

    entity_name = " ".join(
        word.capitalize()
        for word in words
    )

    return entity_name