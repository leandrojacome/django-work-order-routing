import json

from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from work_orders.application.route_work_order import KeywordRoutingStrategy, RouteWorkOrder
from work_orders.domain.work_order import WorkOrder


@csrf_exempt
def route_work_order(request: HttpRequest) -> JsonResponse:
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)
    payload = json.loads(request.body)
    decision = RouteWorkOrder(KeywordRoutingStrategy()).execute(
        WorkOrder(payload["id"], payload["summary"], int(payload["urgency"]))
    )
    return JsonResponse({"specialty": decision.specialty, "priority": decision.priority})
