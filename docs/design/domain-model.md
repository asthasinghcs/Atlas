# Atlas Domain Model

The domain model defines the core objects Atlas operates on.

---

# Document

## Definition

A document is the atomic unit of information entering Atlas.

Examples:

- News Article
- Research Paper
- Government Announcement

## Fields

- id
- title
- content
- source
- source_type
- url
- published_at
- ingested_at

## Why It Exists

Every piece of intelligence in Atlas originates from a document.

---

# Entity

## Definition

A real-world thing recognized by Atlas.

Examples:

- OpenAI
- Microsoft
- GPT-5
- India
- Semiconductor Industry

## Fields

- id
- name
- type
- aliases
- first_seen
- last_seen

## Why It Exists

Entities become nodes in the knowledge graph.

---

# Relationship

## Definition

A fact connecting two entities.

Example:

OpenAI -> RELEASED -> GPT-5

## Fields

- id
- source_entity_id
- relationship_type
- target_entity_id
- supporting_documents
- confidence

## Why It Exists

Relationships become edges in the knowledge graph.
---

# Trend

## Definition

A trend represents a topic, technology, company, policy area, or concept that is showing meaningful change over time.

Examples:

- AI Agents
- Semiconductor Manufacturing
- Quantum Computing
- Nuclear Fusion

## Fields

- id
- name
- description
- trend_score
- confidence_score
- contradiction_score
- first_detected_at
- last_updated_at

## Why It Exists

Trends are one of the primary outputs of Atlas.

They convert isolated facts into actionable intelligence.
---

# Evidence

## Definition

Evidence represents supporting or contradicting information associated with a trend, relationship, or report.

Examples:

- News article
- Research paper
- Government announcement

## Fields

- id
- document_id
- evidence_type
- excerpt
- relevance_score
- stance

## Stance Values

- SUPPORTING
- CONTRADICTING
- NEUTRAL

## Why It Exists

Atlas should never make claims without evidence.

Every conclusion must be traceable to source material.
---

# Evidence

## Definition

Evidence represents supporting or contradicting information associated with a trend, relationship, or report.

Examples:

- News article
- Research paper
- Government announcement

## Fields

- id
- document_id
- evidence_type
- excerpt
- relevance_score
- stance

## Stance Values

- SUPPORTING
- CONTRADICTING
- NEUTRAL

## Why It Exists

Atlas should never make claims without evidence.

Every conclusion must be traceable to source material.