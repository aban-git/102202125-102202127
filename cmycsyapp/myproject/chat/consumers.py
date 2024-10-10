import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from .models import ChatMessage
from .serializers import ChatMessageSerializer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.me = self.scope['user']
        self.other_username = self.scope['url_route']['kwargs']['username']
        self.other_user = await self.get_user(self.other_username)

        if self.other_user is None:
            await self.close()
        else:
            # 创建一个唯一的房间名
            self.room_name = f'chat_{min(self.me.id, self.other_user.id)}_{max(self.me.id, self.other_user.id)}'
            self.room_group_name = f'chat_{self.room_name}'

            # 加入房间组
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

            await self.accept()

    async def disconnect(self, close_code):
        # 离开房间组
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # 接收来自 WebSocket 的消息
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message')

        if message:
            # 保存消息到数据库
            chat_message = await self.create_chat_message(self.me, self.other_user, message)
            serialized_message = ChatMessageSerializer(chat_message).data

            # 发送消息到房间组
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': serialized_message
                }
            )

    # 接收来自房间组的消息
    async def chat_message(self, event):
        message = event['message']

        # 发送消息到 WebSocket
        await self.send(text_data=json.dumps(message))

    @database_sync_to_async
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    @database_sync_to_async
    def create_chat_message(self, sender, receiver, message):
        return ChatMessage.objects.create(sender=sender, receiver=receiver, message=message)
