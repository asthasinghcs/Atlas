NORMALIZATION_MAP = {

    "Google's": "Google",
    "Google Search": "Google",
    "Google Search Console": "Google",

    "Meta Platforms": "Meta",
    "Facebook": "Meta",

    "Adobe Photoshop": "Adobe",
    "Photoshop": "Adobe",

    "YouTube SEO": "YouTube",

    "OpenAI Codex": "OpenAI",
    "ChatGPT": "OpenAI",

    "Amazon AWS": "Amazon",
    "AWS": "Amazon",

    "Microsoft Word": "Microsoft",
    "Microsoft Office": "Microsoft"
}


def normalize_entity(
    entity_name: str
):

    return NORMALIZATION_MAP.get(
        entity_name,
        entity_name
    )