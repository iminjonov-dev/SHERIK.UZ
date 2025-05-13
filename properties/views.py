from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from properties.models import Comment
from properties.serializer import CommentModelSerializer,CommentListModelSerializer


# Create your views here.
class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentModelSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        print("perform_create chaqirildi")  # Terminalda chiqishini tekshirish uchun
        serializer.save()
class CommentListAPIView(ListAPIView):
    serializer_class = CommentListModelSerializer
    queryset = Comment.objects.all()

class CommentDetailView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListModelSerializer
    lookup_field = "id"