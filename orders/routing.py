from django.urls import path
from orders.consumers import NotificationConsumer, NotificationTenant

websocket_urlpatterns = [
    path("ws/notifications/owner/<int:user_id>/", NotificationConsumer.as_asgi()),
    path("ws/notifications/tenant/<int:user_id>/", NotificationTenant.as_asgi()),
]
