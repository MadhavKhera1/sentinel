from app.domain.incident_state_machine import (
    IncidentStateMachine,
)
from app.domain.incident_status import IncidentStatus


print(
    IncidentStateMachine.is_valid_transition(
        IncidentStatus.DETECTED,
        IncidentStatus.DIAGNOSING
    )
)

print(
    IncidentStateMachine.is_valid_transition(
        IncidentStatus.DETECTED,
        IncidentStatus.RESOLVED
    )
)