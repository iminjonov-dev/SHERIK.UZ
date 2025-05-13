import random
from django.core.mail import send_mail

def generate_verification_code():
    return str(random.randint(100000, 999999))

def send_verification_email(email, code):
    send_mail(
        'Tasdiqlash kodi',
        f'Sizning tasdiqlash kodingiz: {code}',
        None,
        [email],
        fail_silently=False,
    )
