from rest_framework.serializers import IntegerField,ModelSerializer, ChoiceField, ValidationError,CharField
from orders.models import Bookings
from properties.models import Property  # Property modelini import qilish kerak

class BookingModelSerializer(ModelSerializer):
    total_price = IntegerField(read_only=True)
    class Meta:
        model = Bookings
        fields = ('tenant', 'property', 'start_date', 'end_date', 'rental_type', 'total_price')  # total_price qo'shildi

    def validate(self, attrs):
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')
        rental_type = attrs.get('rental_type')
        property_instance = attrs.get('property')  # Model obyektini olish

        if not start_date or not end_date:
            raise ValidationError("start_date va end_date talab qilinadi")

        day = (end_date - start_date).days
        if day <= 0:
            raise ValidationError("end_date start_date dan keyin bo‘lishi kerak")

        # Narxni hisoblash
        if rental_type == "daily":
            total_price = day * property_instance.price_day
        elif rental_type == "weekly":
            total_price = (day // 7) * property_instance.price_week
        elif rental_type == "monthly":
            if day < 90:
                day += 10  # Chegirma shartlari
            total_price = (day // 30) * property_instance.price_week * 4
        elif rental_type == "yearly":
            total_price = (day // 365) * property_instance.price_year
        else:
            raise ValidationError("Noto‘g‘ri rental_type qiymati")
        # Bookings.objects.create(total_price=total_price)
        # Hisoblangan narxni saqlash uchun atributga qo‘shish
        attrs['total_price'] = total_price

        return attrs
    def create(self, validated_data):
        return Bookings.objects.create(**validated_data)

class SendBookingModelSerializer(ModelSerializer):
    tenant_name = CharField(source='tenant.username', read_only=True)  # Tenant foydalanuvchi nomi
    property_name = CharField(source='property.title', read_only=True)
    class Meta:
        model = Bookings
        fields = ['id', 'tenant_name', 'property_name', 'start_date', 'end_date', 'booking_status','total_price','rental_type']
class BookingUpdateModelSerializer(ModelSerializer):
    class Meta:
        model=Bookings
        fields=['booking_status']