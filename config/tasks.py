from django.contrib.auth import get_user_model

from config.celery import app
from django.core.mail import send_mail

User = get_user_model()

users = User.objects.all()

@app.task
def send_spam():
    send_mail(
        'Здравствуйте, Вас приветствует courses.kg',
        'Мы рады что вы с нами!',
        'musabekova.amina13@gmail.com',
        [user.email for user in users]
    )

@app.task
def send_notifications_about_new_course(course_title):
    """Рассылка уведомлений о новых курсах для всех пользователей"""
    send_mail(
        'Спам',
        f'Привет, опубликован новый курс! {course_title}',
        'musabekova.amina13@gmail.com',
        [user.email for user in users]
    )
