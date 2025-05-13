from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, login, Users, LoginSerializer, login_view, register_view, LogoutView, verify_code_view
from django.urls import path
from . import views

urlpatterns = [

    # api url
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/list/', Users.as_view(), name='users'),
    path('api/register12/', register_view, name='register'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/verify/', verify_code_view),

]
