# Entity

Purpose:
Represents a real-world object discovered inside a document.

Examples:

Company
Technology
Person
Country
Organization
Product

Examples:

NVIDIA
OpenAI
Taiwan
TSMC
GPT-5

Fields

id
name
entity_type
created_at

Relationships

Document -> contains -> Entity
Entity -> mentioned_in -> Document