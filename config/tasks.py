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
    """Спам рассылка для всех пользователей"""
    send_mail(
        'Спам',
        f'Привет, хочешь записаться на курсы? Заходи на наш сайт: {http://127.0.0.1:8000/api/v1/purchases/}',
        'musabekova.amina13@gmail.com',
        email
    )


@app.task
def send_notifications_about_new_course(course_title):
    """Рассылка уведомлений о новых курсах для всех пользователей"""
    send_mail(
        'Спам',
        f'Привет, опубликован новый курс! {course_title}',
        'musabekova.amina13@gmail.com',
        email
    )
