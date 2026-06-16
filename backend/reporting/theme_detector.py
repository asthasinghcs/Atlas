from collections import defaultdict

from sqlalchemy.orm import Session

from sqlalchemy import func

from models.entity import Entity
from models.document_entity import DocumentEntity


THEMES = {
    "Artificial Intelligence": [
        "OpenAI",
        "ChatGPT",
        "Claude",
        "Anthropic",
        "Google Gemini",
        "Gemini",
        "Microsoft Copilot",
        "AI"
    ],

    "Cloud Computing": [
        "Amazon",
        "AWS",
        "Google Cloud",
        "Microsoft Azure",
        "Cloudflare"
    ],

    "Digital Marketing": [
        "SEO",
        "PPC",
        "Google Analytics",
        "Google AdSense",
        "Yoast SEO",
        "WordPress"
    ],

    "Social Media": [
        "YouTube",
        "LinkedIn",
        "Facebook",
        "Instagram",
        "Twitter"
    ],

    "E-Commerce": [
        "Amazon",
        "Shopify",
        "WooCommerce"
    ]
}


def detect_themes(
    db: Session
):

    entity_mentions = defaultdict(int)

    rows = (
        db.query(
            Entity.name,
            func.count(
                DocumentEntity.id
            )
        )
        .join(
            DocumentEntity,
            Entity.id == DocumentEntity.entity_id
        )
        .group_by(
            Entity.name
        )
        .all()
    )

    for name, mentions in rows:

        entity_mentions[name] = mentions

    theme_scores = []

    for theme, entities in THEMES.items():

        score = 0

        matched_entities = []

        for entity in entities:

            mentions = entity_mentions.get(
                entity,
                0
            )

            if mentions > 0:

                score += mentions

                matched_entities.append(
                    {
                        "entity": entity,
                        "mentions": mentions
                    }
                )

        if score > 0:

            theme_scores.append(
                {
                    "theme": theme,
                    "score": score,
                    "entities": matched_entities
                }
            )

    theme_scores.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return theme_scores