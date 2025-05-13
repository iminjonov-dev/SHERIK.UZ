from modeltranslation.translator import register, TranslationOptions
from .models import ChatMessage


@register(ChatMessage)
class ChatMessageTranslationOptions(TranslationOptions):
    fields = (
        'message_text',
    )

