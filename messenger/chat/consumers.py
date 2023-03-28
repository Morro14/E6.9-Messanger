import json


from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Chat


class ChatConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chat_name = None
        self.chat_group_name = None
        self.chat = None
        
    def connect(self):
        self.chat_name = self.scope['url_route']['kwargs']['chat_name']
        self.chat = Chat.objects.get(name=self.chat_name)
        self.chat_group_name = f'chat_{self.chat_name}'
        
        self.accept()
        
        async_to_sync(self.channel_layer.group_add)(
            self.chat_group_name,
            self.channel_name,
            
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.chat_group_name,
            self.channel_name,
        )
        
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = text_data_json['username']
        
        async_to_sync(self.channel_layer.group_send)(
            self.chat_group_name,
            {
                'type':'chat_message',
                'message': message,
                'username': user
            }
        )
        
    def chat_message(self, event):
        self.send(text_data=json.dumps(event))
        
