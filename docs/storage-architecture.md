# Atlas Storage Architecture

## Overview

Atlas uses three storage systems because different types of data have different access patterns.

- PostgreSQL
- Neo4j
- Qdrant

---

# PostgreSQL

## Purpose

Store structured application data.

## Stores

### Documents

- id
- title
- content
- source
- source_type
- url
- published_at
- ingested_at

### Reports

- id
- title
- summary
- confidence_score
- contradiction_score
- generated_at

### Evidence Metadata

- document references
- relevance scores
- report mappings

## Why PostgreSQL

Strong consistency.

Reliable querying.

Structured data.

Transactional guarantees.

---

# Neo4j

## Purpose

Store relationships between entities.

## Stores

### Entities

Examples:

- OpenAI
- Microsoft
- GPT-5
- India

### Relationships

Examples:

OpenAI -> RELEASED -> GPT-5

Microsoft -> PARTNERS_WITH -> OpenAI

India -> INVESTS_IN -> Semiconductor Manufacturing

## Why Neo4j

Graph traversal is a core Atlas workload.

Questions like:

Which companies are connected to AI infrastructure through multiple hops?

are easier in Neo4j than relational databases.

---

# Qdrant

## Purpose

Store vector embeddings.

## Stores

### Document Embeddings

Semantic representations of documents.

### Evidence Embeddings

Semantic representations of evidence snippets.

## Why Qdrant

Enables semantic retrieval.

Find similar content even when wording differs.

---

# Data Ownership

## PostgreSQL

Source of truth for:

- Documents
- Reports

## Neo4j

Source of truth for:

- Entities
- Relationships

## Qdrant

Source of truth for:

- Embeddings

---

# Retrieval Flow

User Query

→ Qdrant Retrieval

→ Relevant Documents

→ PostgreSQL Metadata

→ Neo4j Relationship Exploration

→ Report Generation