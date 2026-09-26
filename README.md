# Work Order Routing with Django

This service routes maintenance work orders to electrical, plumbing, or general teams and derives operational priority from urgency.

## Architecture and patterns

The Work Order Routing bounded context keeps the `WorkOrder` entity and `RoutingDecision` value object independent of Django. `RouteWorkOrder` depends on a Strategy port; the Django view is an inbound adapter. Repository is absent because this focused use case is a pure decision. Visitor would add ceremony to a homogeneous work-order model and is documented as a rejected alternative.

```bash
python -m pip install -e '.[dev]'
pytest
ruff check .
```

`POST /work-orders/route` accepts `id`, `summary`, and urgency from 1 to 5.

See [architecture](docs/architecture.md), [API documentation](docs/api.md), and [ADR-001](docs/adr/001-explicit-routing-strategy.md).
