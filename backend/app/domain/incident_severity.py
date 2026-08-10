from enum import Enum

class IncidentSeverity(Enum):
    """
    Represents the severity of an incident.
    Every incident must always be in exactly one valid state.
    """

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"