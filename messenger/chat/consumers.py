import json


from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Chat, Message, Room


class RoomConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_pk = None
        self.room_group_name = None
        self.room = None
        self.user = None
        
    def connect(self):
        self.room_pk = self.scope['url_route']['kwargs']['room_pk']
        self.room = Room.objects.get(pk=self.room_pk)
        self.room_group_name = f'room_{self.room_pk}'
        self.user = self.scope['user']
        
        self.accept()
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
            
        )
        
        self.send(json.dumps({
            'type': 'user_list',
            'users': [user.username for user in self.room.users.all()],
            
        })
                  )
        
        if self.user.is_authenticated:
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'user_join',
                    'user': self.user.username,
                }
            )
            self.room.users.add(self.user)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )
        
        
        if self.user.is_authenticated:
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'user_leave',
                    'user': self.user.username,
                }
            )
            self.room.users.remove(self.user)
        
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.user.username
        
        if not self.user.is_authenticated:
            return
        
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'room_message',
                'message': message,
                'username': user,
                
            }
        )
        
        # Message.objects.create(user=self.user, content=message, chat=self.chat)
        
    def room_message(self, event):
        self.send(text_data=json.dumps(event))
        
        
    def user_join(self, event):
        self.send(text_data=json.dumps(event))
        
    def user_leave(self, event):
        self.send(text_data=json.dumps(event))


class ChatConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chat_pk = None
        self.chat_group_name = None
        self.chat = None
        self.user = None
        
    def connect(self):
        self.chat_pk = self.scope['url_route']['kwargs']['chat_pk']
        self.chat = Chat.objects.get(pk=self.chat_pk)
        self.chat_group_name = f'chat_{self.chat_pk}'
        self.user = self.scope['user']
        
        self.accept()
        
        async_to_sync(self.channel_layer.group_add)(
            self.chat_group_name,
            self.channel_name,
            
        )
        
        self.send(json.dumps({
            'type': 'user_list',
            'users': [user.username for user in self.chat.users.all()],
            
        })
                  )
        
        if self.user.is_authenticated:
            async_to_sync(self.channel_layer.group_send)(
                self.chat_group_name,
                {
                    'type': 'user_join',
                    'user': self.user.username,
                }
            )
            self.chat.users.add(self.user)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.chat_group_name,
            self.channel_name,
        )
        
        
        if self.user.is_authenticated:
            async_to_sync(self.channel_layer.group_send)(
                self.chat_group_name,
                {
                    'type': 'user_leave',
                    'user': self.user.username,
                }
            )
            self.chat.users.remove(self.user)
        
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.user.username
        
        if not self.user.is_authenticated:
            return
        
        async_to_sync(self.channel_layer.group_send)(
            self.chat_group_name,
            {
                'type':'chat_message',
                'message': message,
                'username': user,
                
            }
        )
        
        Message.objects.create(user=self.user, content=message, chat=self.chat)
        
    def chat_message(self, event):
        self.send(text_data=json.dumps(event))
        
        
    def user_join(self, event):
        self.send(text_data=json.dumps(event))
        
    def user_leave(self, event):
        self.send(text_data=json.dumps(event))
        
