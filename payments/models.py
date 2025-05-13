from django.db import models
from django.db.models import Model, ForeignKey, CASCADE, ManyToManyField, ImageField


class Payment(Model):
    payment_id = models.AutoField(primary_key=True)
    booking_id = models.ForeignKey('Booking', on_delete=models.CASCADE)
    payer_id = models.ForeignKey('User', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Pul miqdori")  # Pul miqdori

    def __str__(self):
        return f"Payment {self.payment_id} - {self.amount}"
