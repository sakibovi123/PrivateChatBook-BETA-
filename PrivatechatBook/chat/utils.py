from .models import *

def find_or_create_privateRoom(user1, user2):
    try:
        chat = PrivateChatRoom.objects.get(user1=user1, user2=user2)
    except PrivateChatRoom.DoesNotExist:
        chat = PrivateChatRoom.objects.get(user1=user2, user2=user1)
    except Exception as e:
        chat = PrivateChatRoom.objects.get(user1=user1, user2=user2)
        chat.save()
    return chat