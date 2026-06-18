import spacy

from extraction.entity_filters import is_valid_entity
from extraction.entity_normalizer import normalize_entity

nlp = spacy.load(
    "en_core_web_sm"
)


ENTITY_MAPPING = {
    "ORG": "Organization",
    "PERSON": "Person",
    "GPE": "Location",
    "LOC": "Location",
    "PRODUCT": "Product",
    "EVENT": "Event"
}


ALLOWED_LABELS = {
    "ORG",
    "GPE",
    "LOC",
    "PRODUCT"
}


def extract_entities(
    text: str
):

    doc = nlp(text)

    entities = []
    seen = set()

    for ent in doc.ents:

        if ent.label_ not in ALLOWED_LABELS:
            continue

        entity_name = normalize_entity(
            ent.text.strip()
        )

        if not is_valid_entity(entity_name):
            continue

        entity_type = ENTITY_MAPPING.get(
            ent.label_
        )

        if entity_type is None:
            continue

        key = (
            entity_name.lower(),
            entity_type
        )

        if key in seen:
            continue

        seen.add(key)

        entities.append(
            {
                "name": entity_name,
                "entity_type": entity_type
            }
        )

    return entities