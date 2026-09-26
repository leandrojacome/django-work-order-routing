# API

## POST /work-orders/route

Request: `{ "id": "wo-1", "summary": "Water leak", "urgency": 5 }`

Response: `{ "specialty": "plumbing", "priority": "urgent" }`. Urgency must be an integer from 1 through 5. Production delivery requires structured validation and authenticated callers.
