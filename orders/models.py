from django.db import models
from django.db.models import Model, ForeignKey, CASCADE
from django.db.models.enums import TextChoices
from django.db.models.fields import DateTimeField, CharField, DecimalField, IntegerField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Bookings(Model):
    class RTYPE(TextChoices):
        DAILY='daily',_('Daily')
        WEEKLY='weekly',_('Weekly')
        MONTHLY='monthly',_('Monthly')
        YEARLY='yearly',_('Yearly')
    class BSTATUS(TextChoices):
        PENDING='pending',_('Pending')
        CONFIRMED='confirmed',_('Confirmed')
        CANCELLED='cancelled',_('Cancelled')
        COMPLETED='completed',_('Completed')
    class PSTATUS(TextChoices):
        NOT_PAID='not paid',_("Not Paid")
        PAID='paid',_("Paid")
        PARTIAL_PAID='partial_paid',_("Partial Paid")
    tenant=ForeignKey('user.User',CASCADE,verbose_name=_('Tenant'))
    property=ForeignKey('properties.Property',CASCADE,verbose_name=_('Property'))
    start_date=DateTimeField(verbose_name=_('Start date'))
    end_date=DateTimeField(verbose_name=_('End date'))
    booking_status=CharField(max_length=30,choices=BSTATUS.choices,default=BSTATUS.PENDING,verbose_name=_('Booking status'))
    payment_status=CharField(max_length=30,choices=PSTATUS.choices,default=PSTATUS.NOT_PAID,verbose_name=_('Payment status'))
    total_price=DecimalField(max_digits=20,decimal_places=2,verbose_name=_('Total Price'))
    discount=IntegerField(verbose_name=_('Discount'),default=0)
    created_at=DateTimeField(auto_now_add=True,verbose_name=_('Created at'))
    updated_at=DateTimeField(auto_now=True,verbose_name=_('Updated at'))
    rental_type=CharField(max_length=30,choices=RTYPE.choices,default=RTYPE.DAILY)
class Notification(models.Model):
    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='notifications')  # Uy egasi
    booking = models.ForeignKey('orders.Bookings', on_delete=models.CASCADE, related_name='notifications')  # Booking
    message = models.CharField(max_length=255)  # Xabar matni
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.owner.username} - {self.message}"
