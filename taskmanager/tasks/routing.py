from django.urls import re_path
from . import consumer

websocket_urlpatterns = [
    re_path(r'ws/data-stream/', consumer.DataStreamConsumer.as_asgi()),
]