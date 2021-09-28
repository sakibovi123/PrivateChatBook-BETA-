from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PrivateChatRoom(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2")

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"A chat Between {user1} and {user2}."
    

    @property
    def group_name(self):
        return f"privateChatRoom-{self.id}"


class RoomChatMessageManager(models.Model):
    def by_room(self, room):
        qs = RoomChatMessage.objects.filter(
            room=room
        ).order_by('-timestamp')


class RoomChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(PrivateChatRoom, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(unique=False, blank=True)

    objects = RoomChatMessageManager()

    def __str__(self):
        return self.content
    
