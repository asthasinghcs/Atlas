def extract_entities(text: str):
    """
    Temporary rule-based entity extraction.
    Later replaced by LLMs and NER models.
    """

    entities = []

    known_entities = {
        "NVIDIA": "Company",
        "OpenAI": "Company",
        "Taiwan": "Country",
        "TSMC": "Company",
        "GPT-5": "Product",
        "AI": "Technology"
    }

    for entity_name, entity_type in known_entities.items():
        if entity_name.lower() in text.lower():
            entities.append(
                {
                    "name": entity_name,
                    "entity_type": entity_type
                }
            )

    return entities