from dataclasses import dataclass
from datetime import datetime
from app.domain.incident_severity import IncidentSeverity
from app.domain.incident_status import IncidentStatus

@dataclass
class Incident:
    """
    Represents an incident in the system.
    Every incident must always be in exactly one valid state.
    """

    incident_id: str
    service_name: str
    incident_type: str
    severity: IncidentSeverity
    status: IncidentStatus
    detected_at: datetime
    recovery_attempts: int= 0
    recommended_action: str= ""
    final_decision: str= ""
    