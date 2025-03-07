# hospital_robot/asgi.py

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from delivery.consumers import MedicineDeliveryConsumer
from django.urls import path

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/medicine_delivery/', MedicineDeliveryConsumer.as_asgi()),
        ])
    ),
})
