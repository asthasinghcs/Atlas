# Atlas Backend Architecture

## Overview

The backend is organized by responsibility.

Each module owns a specific part of the intelligence pipeline.

The architecture follows separation of concerns.

---

# High Level Structure

backend/

├── api/
├── ingestion/
├── extraction/
├── graph/
├── vector/
├── reasoning/
├── reporting/
├── db/
├── models/
├── schemas/
├── services/
└── main.py

---

# api/

## Responsibility

Expose Atlas functionality through REST APIs.

Examples:

- GET /documents
- GET /trends
- POST /reports/generate

## Owns

- Route definitions
- Request handling
- Response handling

## Does Not Own

- Business logic
- Database access

---

# ingestion/

## Responsibility

Collect information from external sources.

Examples:

- RSS feeds
- arXiv
- Government publications

## Owns

- Fetching
- Parsing
- Source adapters

Output:

Document

---

# extraction/

## Responsibility

Convert raw documents into structured information.

## Owns

- Entity extraction
- Relationship extraction

Output:

Entities
Relationships

---

# graph/

## Responsibility

Interact with Neo4j.

## Owns

- Node creation
- Relationship creation
- Graph queries

Input:

Entities
Relationships

Output:

Knowledge Graph

---

# vector/

## Responsibility

Interact with Qdrant.

## Owns

- Embedding creation
- Embedding storage
- Similarity search

Input:

Documents

Output:

Embeddings

---

# reasoning/

## Responsibility

Generate higher-level intelligence.

## Owns

- Trend detection
- Confidence scoring
- Contradiction analysis

Input:

Documents
Entities
Relationships
Evidence

Output:

Insights

---

# reporting/

## Responsibility

Generate final reports.

## Owns

- Report generation
- Evidence aggregation
- Source attribution

Input:

Insights
Evidence

Output:

Report

---

# db/

## Responsibility

PostgreSQL access layer.

## Owns

- Database sessions
- Database configuration
- Persistence utilities

---

# models/

## Responsibility

Database models.

Examples:

- Document
- Report
- Evidence

Purpose:

Represent persisted data.

---

# schemas/

## Responsibility

API contracts.

Examples:

- DocumentResponse
- TrendResponse
- ReportResponse

Purpose:

Validate requests and responses.

---

# services/

## Responsibility

Business logic.

Examples:

- TrendService
- ReportService
- EntityService

Purpose:

Coordinate multiple modules.

---

# main.py

## Responsibility

Application entry point.

Purpose:

Start FastAPI application.

Register routes.

Initialize dependencies.

---

# Dependency Flow

api
↓
services
↓
db / graph / vector / reasoning / reporting

Never:

db
↓
api

Never:

graph
↓
api

Dependencies should always point inward.

---

# Design Principles

1. Single Responsibility

Each module should have one clear purpose.

2. Separation of Concerns

Storage, APIs, reasoning, and reporting remain independent.

3. Extensibility

New sources and agents should be added without major rewrites.

4. Testability

Each module should be testable in isolation.