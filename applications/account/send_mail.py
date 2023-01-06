from django.core.mail import send_mail


def send_confirmation_email(email, code):
    activation_url = f'http://localhost:8000/api/v1/account/activate/{code}'
    send_mail(
        'Активация пользователя',
        activation_url,
        'musabekova.amina13@gmail.com',
        [email],
        fail_silently=True
    )