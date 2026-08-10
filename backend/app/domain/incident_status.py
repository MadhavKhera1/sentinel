from enum import Enum

class IncidentStatus(Enum):
    """
    Represents the current lifecycle stage of an incident.
    Every incident must always be in exactly one valid state.
    """

    DETECTED = "Detected"
    DIAGNOSING = "Diagnosing"
    DECISION = "Decision"
    RECOVERING = "Recovering"
    VERIFYING = "Verifying"
    RESOLVED = "Resolved"
    ESCALATED = "Escalated"
