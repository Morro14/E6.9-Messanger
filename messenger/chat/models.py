from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField


class MyUser(AbstractUser):
    def __str__(self):
        return self.username
    profile_picture = ResizedImageField(size=[200, 300], crop=['middle', 'center'])
    slug = models.SlugField()


class ChatUser(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)


class Chat(models.Model):
    def __str__(self):
        return f'chat#{self.pk}'
    users = models.ManyToManyField(through=ChatUser, to=MyUser)
    name = models.TextField(max_length=128, blank=True)
    
    def join(self, user):
        self.users.add(user)
        self.save()
        
    def leave(self, user):
        self.users.remove(user)
        self.save()


class Message(models.Model):
    
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_created=True, auto_now_add=True)
    content = models.TextField(max_length=600)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.user}: {self.content} [{self.timestamp}]'
