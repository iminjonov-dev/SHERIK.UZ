from django.urls import path

from orders.views import BookingCreateAPIView, BookingAboutAPIView, BookingUpdateRentalTypeUpdateAPIView

urlpatterns=[
        path('order/booking/create',BookingCreateAPIView.as_view()),
        path('order/booking/about/<int:id>',BookingAboutAPIView.as_view()),
        path('order/booking/ipdate/<int:id>',BookingUpdateRentalTypeUpdateAPIView.as_view()),
]