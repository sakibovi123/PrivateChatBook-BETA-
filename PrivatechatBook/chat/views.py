from django.http.response import JsonResponse
from chat.utils import find_or_create_privateRoom
from django.shortcuts import render, HttpResponse
from .models import *
from itertools import chain
import json
# Create your views here.


def get_chat_room_url(request, *args, **kwargs):
    user = request.user


    if not user.is_authenticated:
        return HttpResponse("Go login Now")
    context = {}
    room1 = PrivateChatRoom.objects.filter(user1=user, is_active=True)
    room2 = PrivateChatRoom.objects.filter(user2=user, is_active=True)

    rooms = list(chain(room1, room2))
    m_and_f = []
    for room in rooms:
        if room.user1 == user:
            other_user = room.user2
        else:
            other_user = room.user1

        m_and_f.append({
            "message": "",
            "other_user": other_user
        })
    users = User.objects.exclude(username=user.username)
    # context['m_and_f'] = m_and_f
    context = {
        "users": users
    }
    return render(request, "room.html", context)



def create_or_return_private_chat(request, *args, **kwargs):
    user1 = request.user
    paylaod = {}
    if user1.is_authenticated:
        user2_id = request.POST.get('user2_id')
        try:
            user2 = User.objects.get(pk=user2_id)
            chat = find_or_create_privateRoom(user1, user2)
            paylaod['response'] = "Successfully Got the Chat"
            paylaod['chatroom_id'] = chat.id
        except User.DoesNotExist:
            paylaod['response'] = "Something is wrong"
    else:
        paylaod['you cant chat because of something']
    return HttpResponse(json.dumps(paylaod), content_type="application/json")
