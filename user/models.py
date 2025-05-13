from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import timedelta

class User(AbstractUser):
    class ROLE(models.TextChoices):
        TENANT = 'tenant', _('Tenant')
        LANDLORD = 'landlord', _('Landlord')
        ADMIN = 'admin', _('Admin')

    username = models.CharField(max_length=50, unique=False)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE.choices, default=ROLE.TENANT)
    passport_info = models.CharField(max_length=255, null=True, blank=True)
    verified = models.BooleanField(default=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class VerificationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=10)
