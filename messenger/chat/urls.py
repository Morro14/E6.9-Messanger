from django.urls import path
from .views import RoomViewSet, chat_room_view, UserViewSet, ChatViewSet, user_list_view, chat_view, chat_create_view, api_view
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

room_detail = RoomViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('users/', user_list_view, name='user_list'),
    path('<str:username>/', chat_view, name='chat'),
    path('', chat_create_view, name='chat_create'),
    path('room/<str:name>', chat_room_view, name='chat_room_view'),

]
