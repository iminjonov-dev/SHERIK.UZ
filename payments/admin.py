from django.contrib import admin

class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'payment_id',
        'booking_id',
        'payer_id',
        'amount'
    )

    def __str__(self):
        return f'{self.payment_id} - {self.booking_id} - {self.payer_id} - {self.amount}'