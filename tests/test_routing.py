import json

from django.test import Client

from work_orders.application.route_work_order import KeywordRoutingStrategy, RouteWorkOrder
from work_orders.domain.work_order import Specialty, WorkOrder


def test_routes_urgent_leak_to_plumbing() -> None:
    decision = RouteWorkOrder(KeywordRoutingStrategy()).execute(WorkOrder("wo-1", "Water leak", 5))
    assert decision.specialty == Specialty.PLUMBING
    assert decision.priority == "urgent"


def test_django_adapter_exposes_routing_decision() -> None:
    response = Client().post(
        "/work-orders/route",
        data=json.dumps({"id": "wo-2", "summary": "Power outlet failed", "urgency": 2}),
        content_type="application/json",
    )
    assert response.json() == {"specialty": "electrical", "priority": "normal"}
