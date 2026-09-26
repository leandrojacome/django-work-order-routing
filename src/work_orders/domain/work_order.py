from dataclasses import dataclass
from enum import StrEnum


class Specialty(StrEnum):
    ELECTRICAL = "electrical"
    PLUMBING = "plumbing"
    GENERAL = "general"


@dataclass(frozen=True)
class WorkOrder:
    id: str
    summary: str
    urgency: int

    def __post_init__(self) -> None:
        if not self.summary.strip() or self.urgency not in range(1, 6):
            raise ValueError("Summary and urgency from 1 to 5 are required")


@dataclass(frozen=True)
class RoutingDecision:
    specialty: Specialty
    priority: str
