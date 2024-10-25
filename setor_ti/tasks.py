from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@shared_task
def send_info_to_websocket():
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "metricas", {"type": "update_count"}
    )