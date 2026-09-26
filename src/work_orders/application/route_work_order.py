from typing import Protocol

from work_orders.domain.work_order import RoutingDecision, Specialty, WorkOrder


class RoutingStrategy(Protocol):
    def specialty_for(self, order: WorkOrder) -> Specialty: ...


class KeywordRoutingStrategy:
    def specialty_for(self, order: WorkOrder) -> Specialty:
        text = order.summary.lower()
        if any(word in text for word in ("power", "outlet", "electrical")):
            return Specialty.ELECTRICAL
        if any(word in text for word in ("leak", "pipe", "water")):
            return Specialty.PLUMBING
        return Specialty.GENERAL


class RouteWorkOrder:
    def __init__(self, strategy: RoutingStrategy) -> None:
        self._strategy = strategy

    def execute(self, order: WorkOrder) -> RoutingDecision:
        return RoutingDecision(self._strategy.specialty_for(order), "urgent" if order.urgency >= 4 else "normal")
