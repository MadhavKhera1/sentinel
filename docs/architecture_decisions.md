# ADR-001

## Decision
The Incident domain object will protect its own state transitions but will not execute recovery logic.

## Why
Keeps business rules inside the entity while avoiding a God Object.

## Alternatives
1. Put all logic inside Incident.
2. Put all logic inside IncidentService.

## Decision
Hybrid approach selected.
