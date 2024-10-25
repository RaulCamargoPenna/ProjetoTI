from django.urls import path
from .consumers import ConsumerMetricas

websocket_urlpatterns = [
    path('ws/metricas', ConsumerMetricas.as_asgi())
]