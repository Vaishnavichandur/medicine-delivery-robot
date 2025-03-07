from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/medicine_delivery/', consumers.MedicineDeliveryConsumer.as_asgi()), 
]
