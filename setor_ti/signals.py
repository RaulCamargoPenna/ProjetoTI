from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import CallbacksTeste, TokensTeste
from .tasks import send_info_to_websocket

channel_layer = get_channel_layer()

@receiver(post_save, sender=CallbacksTeste)
def update_callbacks_count(sender, instance, **kwargs):
    # async_to_sync(channel_layer.group_send)(
    #     "metricas", {"type": "update_count"}
    # )
    send_info_to_websocket.delay() 
    
# @receiver(post_save, sender=TokensTeste)
# def update_tokens_info(sender, instance, **kwargs):
#     # async_to_sync(channel_layer.group_send)(
#     #     "metricas", {"type": "update_count"}
#     # )
    send_info_to_websocket.delay()