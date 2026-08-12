from app.domain.incident_status import IncidentStatus

class IncidentStateMachine:
    """
    Validates whether an incident can move from one state to another.
    """

    _ALLOWED_TRANSITIONS = {
        IncidentStatus.DETECTED: {
            IncidentStatus.DIAGNOSING
        },
        IncidentStatus.DIAGNOSING: {
            IncidentStatus.DECISION
        },
        IncidentStatus.DECISION: {
            IncidentStatus.RECOVERING,
            IncidentStatus.ESCALATED
        },
        IncidentStatus.RECOVERING: {
            IncidentStatus.VERIFYING,
            IncidentStatus.ESCALATED
        },
        IncidentStatus.VERIFYING: {
            IncidentStatus.RESOLVED,
            IncidentStatus.RECOVERING,
            IncidentStatus.ESCALATED
        },
        IncidentStatus.RESOLVED: set(),
        IncidentStatus.ESCALATED: set()
    }

    @classmethod
    def is_valid_transition(
        cls,
        current_State: IncidentStatus,
        target_state: IncidentStatus
    ) -> bool:
        allowed = cls._ALLOWED_TRANSITIONS.get(current_State, set())

        return target_state in allowed