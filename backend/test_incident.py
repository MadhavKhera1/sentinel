from datetime import datetime

from app.domain.incident import Incident
from app.domain.incident_status import IncidentStatus
from app.domain.incident_severity import IncidentSeverity


incident = Incident(
    incident_id="INC-0001",
    service_name="Redis",
    incident_type="High Latency",
    severity=IncidentSeverity.HIGH,
    status=IncidentStatus.DETECTED,
    detected_at=datetime.now(),
)

print(incident)