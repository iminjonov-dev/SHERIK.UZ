import json
from channels.generic.websocket import AsyncWebsocketConsumer

import json
from channels.generic.websocket import AsyncWebsocketConsumer
class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope["url_route"]["kwargs"]["user_id"]
        self.group_name = f"user_{self.user_id}"

        # Foydalanuvchini Redis guruhiga qo‘shamiz
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Guruhdan chiqaramiz
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.send(text_data=json.dumps({"message": data["message"]}))

    async def send_notification(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))


class NotificationTenant(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope["url_route"]["kwargs"]["user_id"]
        self.group_name = f"notifications_{self.user_id}"

        # 🔹 WebSocket kanaliga qo‘shilish
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # 🔹 WebSocket kanalidan chiqish
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def send_notification(self, event):
        message = event["message"]

        # 🔹 Frontendga bildirishnoma yuboramiz
        await self.send(text_data=json.dumps({"message": message}))

