from django.db import models
from django.db.models import Model, ForeignKey, CASCADE, ManyToManyField, ImageField

from django.db import models

class ChatMessage(models.Model):
    message_id = models.AutoField(primary_key=True)
    sender_id = models.ForeignKey('User', on_delete=models.CASCADE, related_name='sent_messages', verbose_name='Xabar yuboruvchi')  # Xabar yuboruvchi
    recipient_id = models.ForeignKey('User', on_delete=models.CASCADE, related_name='received_messages', verbose_name='Xabar qabul qiluvchi')  # Qabul qiluvchi
    booking_id = models.ForeignKey('Booking', on_delete=models.SET_NULL, null=True, blank=True)  # Majburiy emas
    property_id = models.ForeignKey('Property', on_delete=models.SET_NULL, null=True, blank=True)  # Majburiy emas
    message_text = models.TextField()  # Xabar matni
    created_at = models.DateTimeField(auto_now_add=True)  # Yaratilgan vaqt

    def __str__(self):
        return f"From {self.sender_id} to {self.recipient_id}: {self.message_text[:30]}..."
