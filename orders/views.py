from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.models import Bookings
from orders.serializer import BookingModelSerializer, SendBookingModelSerializer, BookingUpdateModelSerializer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class BookingCreateAPIView(CreateAPIView):
    serializer_class = BookingModelSerializer
    queryset = Bookings.objects.all()

    def perform_create(self, serializer):
        booking = serializer.save()
        user_id = booking.property.owner_id  # User ID ni modelingizdan oling
        tenant_name=booking.tenant.username
        property_title=booking.property.title

        # Redis orqali xabar jo‘natamiz
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"user_{user_id}",
            {"type": "send_notification", "message": f"{tenant_name} sizning {property_title} uyingizni bron qilmoqchi. "},
        )


class BookingAboutAPIView(APIView):
    def get(self,request,id):
        booking=Bookings.objects.filter(id=id)
        serializer=SendBookingModelSerializer(booking,many=True)
        return Response(serializer.data)
class BookingUpdateRentalTypeUpdateAPIView(UpdateAPIView):
    serializer_class = BookingUpdateModelSerializer
    queryset = Bookings.objects.all()
    lookup_field = 'id'

    def perform_update(self, serializer):
        booking = serializer.save()

        # 🔹 Bookingni yaratgan userni topamiz
        user_id = booking.tenant.id  # Bookingni kim qilgan bo‘lsa, o‘sha userga xabar boradi
        if booking.booking_status=='confirmed':
            message=(f"Ijara bo'yicha uy egasiga jo'natgan so'rovingizni uy egasi TASDIQLADI!\n"
                     f"Uy: {booking.property.title}\n"
                     f"Status: {booking.booking_status} ")
        elif booking.booking_status=='cancelled':
            message = (f"Ijara bo'yicha uy egasiga jo'natgan so'rovingizni uy egasi BEKOR QILDI!.\n"
                       f"Uy: {booking.property.title}\n"
                       f"Status: {booking.booking_status} ")
        else:
            message = (f"Uy: {booking.property.title}\n"
                       f"Status: {booking.booking_status} ")


        # 🔹 WebSocket orqali userga bildirishnoma jo‘natamiz
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"notifications_{user_id}",
            {
                "type": "send_notification",
                "message": f"{message}",
            },
        )

        return JsonResponse({"message": f"Booking statusi yangilandi!  {booking.booking_status}", "status": booking.booking_status})