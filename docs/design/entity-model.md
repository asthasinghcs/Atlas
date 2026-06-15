# Entity

## Purpose

Represents a real-world object discovered inside a document.

Atlas extracts entities from documents and uses them as the building blocks of its knowledge graph.

Examples:

- NVIDIA
- OpenAI
- TSMC
- Taiwan
- GPT-5

---

## Entity Types

Examples:

- Company
- Person
- Technology
- Product
- Country
- Organization

---

## Fields

- id
- name
- entity_type
- created_at

---

## Relationships

Document -> contains -> Entity

Entity -> mentioned_in -> Document

---

## Examples

"NVIDIA launches a new AI chip in Taiwan"

Extracted Entities:

- NVIDIA (Company)
- AI (Technology)
- Taiwan (Country)

These entities can later be connected to build a knowledge graph.