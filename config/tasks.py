from django.contrib.auth import get_user_model

from config.celery import app
from django.core.mail import send_mail

User = get_user_model()
email = []
user = User.objects.all()
for i in user:
    e = i.email
    email.append(e)


@app.task
def send_spam():
    send_mail(
        'Здравствуйте, Вас приветствует courses.kg',
        'Мы рады что вы с нами!',
        'musabekova.amina13@gmail.com',
        email
    )
