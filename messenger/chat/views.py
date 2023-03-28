from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import permissions
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .forms import MessageForm

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
    chat_query = Chat.objects.filter(users=target_user).filter(users=user)
    new_chat = None
    if target_user == user:
        return render(request, template_name='exception.html')
    elif len(chat_query) != 1:
        new_chat = Chat.objects.create()
        new_chat.users.add(user)
        new_chat.users.add(target_user)
        new_chat.name = f'chat_with_{target_user}'
        new_chat.save()

    elif len(chat_query) == 1:
        new_chat = chat_query[0]

    context = {"user": user, "target_user": target_user,
               "chat": new_chat, }

    return render(request, template_name='chat.html', context=context)
