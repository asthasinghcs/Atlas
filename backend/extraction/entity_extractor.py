import spacy

from extraction.entity_normalizer import (
    normalize_entity
)

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


BLOCKED_ENTITIES = {
    "Pros",
    "Cons",
    "Pricing",
    "Features",
    "Benefits",
    "Guide",
    "Tips",
    "Analysis",
    "Review",
    "Background",
    "Background Remover",
    "Magic Resize",
    "Brand Kits",
    "Design",
    "Tools",
    "Tool",
    "Plans",
    "Premium",
    "Run",
    "Overall",
    "Reviews",
    "Guarantees",
    "Send",
    "Finds",
    "Limited",
    "Team Plan",
    "Position Tracking",
    "White Label",
    "Personalize Personalize"
}


def extract_entities(
    text: str
):

    doc = nlp(text)

    entities = []
    seen = set()

    for ent in doc.ents:

        entity_name = normalize_entity(
            ent.text.strip()
        )

        if ent.label_ not in ALLOWED_LABELS:
            continue

        if len(entity_name) < 3:
            continue

        if entity_name in BLOCKED_ENTITIES:
            continue

        if entity_name.isdigit():
            continue

        if len(entity_name.split()) > 6:
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