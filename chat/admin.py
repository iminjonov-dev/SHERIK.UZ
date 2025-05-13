from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from modeltranslation.admin import TranslationAdmin
from chat.models import ChatMessage

@admin.register(ChatMessage)
class ChatAdmin(TranslationAdmin):
    list_display = ('message_id',
                    'sender_id',
                    'recipient_id',
                    'booking_id',
                    'property_id',
                    'message_text',
                    'created_at'
                    )

    def __str__(self):
        return f' {self.sender_id} from {self.recipient_id} message: {self.message_text}'