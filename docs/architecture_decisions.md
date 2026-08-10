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

# ADR-002

## Decision

Keep IncidentStatus and IncidentSeverity inside the domain folder instead of creating a separate value_objects folder.

## Why

These enums belong only to the Incident domain. Creating a dedicated folder for just two files would introduce unnecessary complexity and reduce cohesion.

## Alternatives Considered

Create a separate value_objects folder.

## Why Rejected

Adds folder complexity without providing meaningful architectural benefits at the current project size.