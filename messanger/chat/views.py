from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import permissions

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
    








