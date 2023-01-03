from django.core.mail import send_mail
from loguru import logger

from config.celery import app


@app.task
def send_purchase_confirmation_email(email, title, price, confirmation_code):
    logger.info('A message for confirm the purchase of the course has been sent')
    full_link = f'Click on the link to confirm the purchase of the course "{title}" worth {price}: ' \
                f'http://localhost:8000/api/v1/purchases/confirm/{confirmation_code}'
    send_mail(
        'Confirmation of purchase',
        full_link,
        'aliyakomanovaa@gmail.com',
        [email]
    )
