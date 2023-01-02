from django.urls import path

from . import consumers


ws_patterns = [
    path('test/', consumers.EchoConsumer.as_asgi()),
    path('test/ac/', consumers.MySocket.as_asgi()),]
