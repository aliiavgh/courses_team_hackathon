from django.core.mail import send_mail


def send_confirmation_code(email, code):
    send_mail(
        'Восстановление пароля',
        code,
        'musabekova.amina13@gmail.com',
        [email],
        fail_silently=True
    )
