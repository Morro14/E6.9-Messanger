from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import  ResizedImageField


class MyUser(AbstractUser):
    def __str__(self):
        return self.username
    profile_picture = ResizedImageField(size=[200, 300], crop=['middle', 'center'])
    slug = models.SlugField()
    
    # def save(self, *args, **kwargs):
    #     if self.profile_picture:
    #         self.profile_picture = get_thumbnail(self.profile_picture, '500x600', format='JPEG')
    #     super(MyUser, self).save(*args, **kwargs)
    


class ChatUser(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)
    


class Chat(models.Model):
    def __str__(self):
        return f'chat#{self.pk}'
    users = models.ManyToManyField(through=ChatUser, to=MyUser)
    name = models.TextField(max_length=100, blank=True)


class Message(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_created=True, auto_now_add=True)
    body = models.TextField(max_length=600)
