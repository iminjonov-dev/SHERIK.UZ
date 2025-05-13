from django.contrib import admin
from django.contrib.admin import ModelAdmin

from orders.models import Bookings


# Register your models here.
@admin.register(Bookings)
class AmenitiesAdmin(ModelAdmin):
    list_display = ('tenant','property','start_date','end_date',
                    'booking_status','payment_status',
                    'total_price','discount')