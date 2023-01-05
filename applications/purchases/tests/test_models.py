import re
from datetime import date

from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase
from django.urls import reverse

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
        test_course_1 = Course.objects.create(title='Course_1', description='content', teacher=test_teacher,
                                              subject=test_subject, status='online', available_places=20, discount=20,
                                              start_date=date(2023, 1, 10), end_date=date(2023, 1, 30), price=1000)
        test_course_1.save()
        test_course_2 = Course.objects.create(title='Course_2', description='content', teacher=test_teacher,
                                              subject=test_subject, status='online', available_places=20, discount=20,
                                              start_date=date(2023, 1, 1), end_date=date(2023, 1, 30), price=1000)
        test_course_2.save()

        test_purchase_1 = Purchase.objects.create(id=1, course=test_course_1, student=test_student,
                                                  is_confirm=False)
        test_purchase_1.save()

    def test_purchase_status(self):
        purchase_1 = Purchase.objects.get(id=1)
        self.assertEqual(purchase_1.status, 'not_confirmed')

