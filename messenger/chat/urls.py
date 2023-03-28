from django.urls import path
from .views import UserViewSet, ChatViewSet, user_list_view, chat_view
from rest_framework import renderers


user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

chat_detail = ChatViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('users/', user_list_view, name='user_list'),
    path('<str:username>/', chat_view, name='chat'),
]
