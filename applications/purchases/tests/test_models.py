from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase

from model_bakery import baker

from applications.courses.models import Subject, Course
from applications.purchases.models import Purchase

User = get_user_model()


class PurchaseTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_student = User.objects.create(email='student@gmail.com', password='neverland110')
        test_student.save()
        test_teacher = User.objects.create_user(email='teacher@gmail.com', password='mrrobot990')
        test_teacher.save()
        test_subject = Subject.objects.create(name='subject_1')
        test_subject.save()
        test_course = Course.objects.create(title='Course_1', description='content', teacher=test_teacher,
                                            subject=test_subject, status='online', available_places=20, discount=20,
                                            start_date=date(2023, 1, 10), end_date=date(2023, 1, 30), price=1000)
        test_course.save()
        test_purchase = baker.make('purchases.Purchase', course=test_course, student=test_student,
                                   status='not_confirmed', created_at=date.today())
        test_purchase.save()


