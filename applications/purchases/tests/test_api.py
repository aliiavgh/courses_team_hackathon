from datetime import date
from random import randrange

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from model_bakery import baker

from applications.courses.models import Course, Subject
from applications.courses.serializers import CourseSerializer
from applications.purchases.models import Purchase
from applications.purchases.permissions import IsPurchaseOwner

User = get_user_model()


class PurchaseAPITestCAse(APITestCase):
    @classmethod
    def setUpTestData(cls):
        test_student = User.objects.create(email='student@gmail.com', password='neverland110')
        test_student.save()
        test_teacher = User.objects.create_user(email='teacher@gmail.com', password='mrrobot990')
        test_teacher.save()
        test_subject = Subject.objects.create(name='subject_1')
        test_subject.save()
        test_student.user_permission.add(IsPurchaseOwner)
        test_course = Course.objects.create(title='Course_1', description='content', teacher=test_teacher,
                                            subject=test_subject, status='online', available_places=20, discount=20,
                                            start_date=date(2023, 1, 10), end_date=date(2023, 1, 30), price=1000)
        test_course.save()
        test_purchases = baker.make('purchases.Purchase', course=test_course, student=test_student,
                                    status='not_confirmed', created_at=date.today(), _quantity=5)
        test_purchases.save()

    def can_student_read_purchase_courses_list(self):
        purchases = Purchase.objects.all()
        response = self.client.get(reverse('purchases-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
