# Changelog

All notable changes to Atlas will be documented in this file.

The project follows a milestone-based development process where each release represents a complete engineering milestone rather than incremental work.

---

## v0.7.0 - Intelligence Engine Foundation

### Added

- Entity Intelligence service for centralized entity analysis.
- Trend Engine for entity trend classification.
- Historical comparison engine.
- Confidence scoring engine.
- Snapshot builder for historical intelligence data.
- Trend snapshot database model and schema.

### Changed

- Refactored Dashboard to consume the centralized intelligence service.
- Refactored Influence API to reuse the intelligence pipeline.
- Refactored Intelligence Report around a canonical entity object.
- Renamed `trend_detector.py` to `trend_classifier.py` for clearer separation of responsibilities.

### Architecture

- Eliminated duplicated entity-ranking logic across multiple APIs.
- Established a reusable intelligence layer shared across reporting endpoints.
- Completed the backend intelligence foundation for future React visualizations and analytics.