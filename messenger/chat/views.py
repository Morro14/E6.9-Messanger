from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, mixins
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


from .serializers import *
from .models import *


class UserViewSet(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class ChatViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAdminUser]
    
    
  
class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def create(self, request, *args, **kwargs):
        room = Room.objects.create(name=request.POST.get('name'))
        room.save()
        


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAdminUser]


def user_list_view(request):
    return render(request, template_name='user_list.html')


@login_required
def chat_view(request, username):
    user = request.user
    target_user = MyUser.objects.get(username=username)
    chat=None

    chat, created = Chat.objects.get_or_create(name=f'Chat with {target_user}')
    if target_user == user:
        return render(request, template_name='exception.html', context={'exception':'Cannot start chat with yourself'})

    context = {"user": user, "target_user": target_user,
               "chat": chat, }
    return render(request, template_name='chat.html', context=context)


@login_required
def chat_room_view(request, name):
    user = request.user
    room, created = Room.objects.get_or_create(name=name)  
        
    context = {"user": user, 
               "room": room,
            }

    return render(request, template_name='chat_room.html', context=context)


def chat_create_view(request):
    return render(request, template_name='chat_main.html')



