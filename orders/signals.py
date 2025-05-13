from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import Bookings, Notification

@receiver(post_save, sender=Bookings)
def create_booking_notification(sender, instance, created, **kwargs):
    if created:  # Faqat yangi booking yaratilganda ishlaydi
        owner = instance.property.owner  # Uy egasini avtomatik aniqlash
        tenant_name = instance.tenant.username
        property_name = instance.property.title

        # Uy egasiga bildirishnoma yaratish
        Notification.objects.create(
            owner=owner,
            booking=instance,
            message=f"📢 {tenant_name} sizning '{property_name}' uyingizni ijaraga oldi!"
        )
