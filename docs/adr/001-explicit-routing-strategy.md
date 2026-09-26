# ADR-001: Isolate routing as a Strategy

## Status
Accepted.

## Decision
The use case receives a `RoutingStrategy` instead of embedding keywords in the Django view.

## Consequences
Framework delivery and routing policy evolve independently. More advanced strategies still need explicit evaluation and fallback behavior.
