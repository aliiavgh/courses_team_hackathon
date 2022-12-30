from django.core.mail import send_mail

from config.celery import app


@app.task
def send_purchase_confirmation_email(email, confirmation_code):
    full_link = f'http://localhost:8000/api/v1/purchases/confirm/{confirmation_code}'
    send_mail(
        'Click on the link and confirm the purchase.',
        full_link,
        'aliyakomanovaa@gmail.com',
        [email]
    )
