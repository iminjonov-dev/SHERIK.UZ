from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from rest_framework_simplejwt.tokens import RefreshToken
import redis
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .serializers import LoginSerializer, RegisterSerializer
from user.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .serializers import LoginSerializer
from django.contrib.auth.models import User

from .models import User
from .serializers import RegisterSerializer, LoginSerializer
#
# class RegisterView(APIView):
#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         email = request.data.get("email")
#
#         if User.objects.filter(username=username).exists():
#             return Response({"error": "Bu username allaqachon mavjud!"}, status=status.HTTP_400_BAD_REQUEST)
#
#         user = User.objects.create_user(username=username, password=password, email=email)
#
#         # Redis'da foydalanuvchi ma'lumotlarini vaqtinchalik saqlaymiz
#         redis_client.setex(f"new_user:{user.id}", 1800, "registered")
#
#         return Response({"message": "Foydalanuvchi muvaffaqiyatli yaratildi!"}, status=status.HTTP_201_CREATED)
#
#
#
# # Redis'ga ulanish
# redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, db=1, decode_responses=True)
#
# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#
#         # Login urinishlari sonini tekshirish (Rate Limiting)
#         attempts = redis_client.get(f"login_attempts:{username}")
#         if attempts and int(attempts) >= 5:
#             return Response({"error": "Ko‘p urinishlar! 5 daqiqadan keyin urinib ko‘ring."}, status=status.HTTP_429_TOO_MANY_REQUESTS)
#
#         user = authenticate(username=username, password=password)
#         if user:
#             # JWT token yaratish
#             refresh = RefreshToken.for_user(user)
#             access_token = str(refresh.access_token)
#
#             # Tokenni Redis'ga saqlash (10 minut davomida)
#             redis_client.setex(f"user_token:{user.id}", 600, access_token)
#
#             return Response({
#                 "refresh": str(refresh),
#                 "access": access_token,
#             })
#         else:
#             # Agar login urinish muvaffaqiyatsiz bo‘lsa, Redis'da urinishlar sonini oshiramiz
#             redis_client.incr(f"login_attempts:{username}")
#             redis_client.expire(f"login_attempts:{username}", 300)  # 5 daqiqaga urinishlar sonini saqlaymiz
#             return Response({"error": "Username yoki parol xato!"}, status=status.HTTP_401_UNAUTHORIZED)
#



# Redis'ga ulanish
redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, db=1, decode_responses=True)
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']
#
#             # Login urinishlarini Redis orqali tekshiramiz
#             attempts = redis_client.get(f"login_attempts:{username}")
#             if attempts and int(attempts) >= 5:
#                 return Response({"error": "Ko‘p urinishlar! 5 daqiqadan keyin urinib ko‘ring."}, status=status.HTTP_429_TOO_MANY_REQUESTS)
#
#             user = authenticate(username=username, password=password)
#             if user:
#                 # JWT token yaratish
#                 refresh = RefreshToken.for_user(user)
#                 access_token = str(refresh.access_token)
#
#                 # Tokenni Redis'ga saqlash (10 minut davomida)
#                 redis_client.setex(f"user_token:{user.id}", 600, access_token)
#
#                 return Response({
#                     "refresh": str(refresh),
#                     "access": access_token,
#                 })
#             else:
#                 # Agar login urinish muvaffaqiyatsiz bo‘lsa, Redis'da urinishlar sonini oshiramiz
#                 redis_client.incr(f"login_attempts:{username}")
#                 redis_client.expire(f"login_attempts:{username}", 300)  # 5 daqiqaga urinishlar sonini saqlaymiz
#                 return Response({"error": "Username yoki parol xato!"}, status=status.HTTP_401_UNAUTHORIZED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @extend_schema(request=LoginSerializer)
# @api_view(['POST'])
# def login_view(request):  # Funksiya nomini `login_view` deb o‘zgartirdik
#     serializer = LoginSerializer(data=request.data)
#     if serializer.is_valid():
#         username = serializer.validated_data['username']
#         password = serializer.validated_data['password']
#
#         # Foydalanuvchini autentifikatsiya qilish
#         user = authenticate(username=username, password=password)
#         if user:
#             login(request, user)  # Foydalanuvchini tizimga kiritish
#             return Response({"message": "Login muvaffaqiyatli amalga oshirildi!"}, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "Username yoki parol noto‘g‘ri!"}, status=status.HTTP_401_UNAUTHORIZED)
#
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#
# @extend_schema(request=RegisterSerializer)
# @api_view(['POST'])
# def register_view(request):
#     serializer = RegisterSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "Ro‘yxatdan o‘tish muvaffaqiyatli!"}, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, VerifyCodeSerializer
from .models import User, VerificationCode

@api_view(['POST'])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Ro‘yxatdan o‘tish muvaffaqiyatli! Emailga tasdiqlash kodi yuborildi."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def verify_code_view(request):
    serializer = VerifyCodeSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        code = serializer.validated_data['code']
        try:
            user = User.objects.get(email=email)
            verification = VerificationCode.objects.get(user=user)
            if verification.code == code and not verification.is_expired():
                user.verified = True
                user.save()
                verification.delete()  # clear code
                return Response({"message": "Email tasdiqlandi. Endi login qilishingiz mumkin."})
            return Response({"error": "Kod noto‘g‘ri yoki eskirgan."}, status=status.HTTP_400_BAD_REQUEST)
        except (User.DoesNotExist, VerificationCode.DoesNotExist):
            return Response({"error": "Foydalanuvchi yoki kod topilmadi."}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







@api_view(['POST'])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(username=email, password=password)  # Email orqali autentifikatsiya qilamiz

        if user:
            login(request, user)
            return Response({"message": "Login muvaffaqiyatli amalga oshirildi!"}, status=status.HTTP_200_OK)
        return Response({"error": "Email yoki parol noto‘g‘ri!"}, status=status.HTTP_401_UNAUTHORIZED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            # Tokenni o'chiramiz
            request.user.auth_token.delete()
            return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)




class Users(ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer