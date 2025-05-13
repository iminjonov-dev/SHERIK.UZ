from django.urls import path

from properties.views import CommentCreateAPIView, CommentListAPIView, CommentDetailView

urlpatterns = [
        path('properties/comment/create',CommentCreateAPIView.as_view()),
        path('properties/comment/list',CommentListAPIView.as_view()),
        path('properties/comment/id/<int:id>',CommentDetailView.as_view())
]
