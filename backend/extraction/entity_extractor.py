import spacy

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
    "Plans"
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

        if len(ent.text.strip()) < 3:
            continue

        if ent.text.strip() in BLOCKED_ENTITIES:
            continue

        entity_type = ENTITY_MAPPING.get(
            ent.label_
        )

        if entity_type is None:
            continue

        key = (
            ent.text.lower(),
            entity_type
        )

        if key in seen:
            continue

        seen.add(key)

        entities.append(
            {
                "name": ent.text.strip(),
                "entity_type": entity_type
            }
        )

    return entities