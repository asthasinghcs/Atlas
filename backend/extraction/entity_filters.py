import re

MIN_LENGTH = 3

INVALID_ENTITIES = {

    "premium",
    "run",
    "overall",
    "reviews",
    "guarantees",
    "pros",
    "cons",
    "team plan",
    "position tracking",
    "white label",
    "personalize personalize",
    "send",
    "finds",
    "limited",

    "program",
    "content",
    "screen",
    "need",
    "magic",
    "note",
    "notes",
    "offer",
    "offers",
    "feature",
    "features",
    "tool",
    "tools",
    "guide",
    "tips",
    "update",
    "updates",
    "version",
    "versions",
    "website",
    "page",
    "pages",
    "post",
    "posts",
    "image",
    "images",
    "video",
    "videos",
    "article",
    "articles",
    "file",
    "files",
    "click",
    "download",
    "login",
    "signup",
    "account",
}


def is_valid_entity(
    entity_name: str
) -> bool:

    if not entity_name:
        return False

    entity_name = entity_name.strip()

    if len(entity_name) < MIN_LENGTH:
        return False

    if entity_name.lower() in INVALID_ENTITIES:
        return False

    if entity_name.isnumeric():
        return False

    if re.fullmatch(r"\d+[kKmMbB]?", entity_name):
        return False

    if len(entity_name.split()) > 6:
        return False

    return True