from django.contrib import admin
from django.urls import path, include
from chat import views


urlpatterns = [
    path("", views.get_chat_room_url, name="Home"),
    path("create_or_return_private_chat/", views.create_or_return_private_chat,name="create_or_return_private_chat"),
]
