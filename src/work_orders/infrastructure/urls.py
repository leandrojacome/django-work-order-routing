from django.urls import path

from work_orders.infrastructure.views import route_work_order

urlpatterns = [path("work-orders/route", route_work_order)]
