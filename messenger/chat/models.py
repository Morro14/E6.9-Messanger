from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    def __str__(self):
        return self.first_name + self.last_name


class ChatUser(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)


class Chat(models.Model):
    users = models.ManyToManyField(through=ChatUser, to=MyUser)


class Message(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_created=True, auto_now_add=True)
    body = models.TextField(max_length=600)
