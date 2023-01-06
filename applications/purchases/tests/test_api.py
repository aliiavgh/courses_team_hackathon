import json
import token
from datetime import date

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from model_bakery import baker

from applications.courses.models import Course, Subject
from applications.purchases.models import Purchase
from applications.purchases.serializers import PurchaseSerializer

User = get_user_model()


class PurchaseAPITestCAse(APITestCase):

    def setUp(self):
        test_student = User.objects.create_superuser(email='student1@gmail.com', password='neverland110')
        test_student.save()
        test_teacher = User.objects.create_superuser(email='teacher@gmail.com', password='mrrobot990')
        test_teacher.save()
        test_subject = Subject.objects.create(name='subject_1')
        test_subject.save()
        test_course = Course.objects.create(title='Course_1', description='content', teacher=test_teacher,
                                            subject=test_subject, status='online', available_places=20, discount=20,
                                            start_date=date(2023, 1, 10), end_date=date(2023, 1, 30), price=1000)
        test_course.save()
        test_purchases = baker.make('purchases.Purchase', course=test_course, student=test_student,
                                    status='not_confirmed', created_at=date.today(), _quantity=5)
        assert test_purchases

        response = self.client.post('/api/v1/account/login/',
                                    {'email': 'student1@gmail.com', 'password': 'neverland110'})
        response_content = json.loads(response.content.decode('utf-8'))
        self.access_token = response_content['access']


    def test_can_get_purchase_courses_list(self):
        purchases = Purchase.objects.all()
        response = self.client.get('http://127.0.0.1:8000/api/v1/purchases/',
                                   HTTP_AUTHORIZATION=f'Bearer {self.access_token}'.format(token))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = PurchaseSerializer(purchases, many=True).data
        self.assertEqual(response.data.get('results'), serializer_data)

    def test_can_get_single_purchase_course(self):
        purchase = Purchase.objects.all()[0]
        response = self.client.get(f'http://127.0.0.1:8000/api/v1/purchases/{purchase.id}/',
                                   HTTP_AUTHORIZATION=f'Bearer {self.access_token}'.format(token))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = PurchaseSerializer(purchase).data
        self.assertEqual(response.data, serializer_data)


class CreatePurchaseAPITestCase(APITestCase):
    def setUp(self):
        test_student = User.objects.create_superuser(email='student@gmail.com', password='neverland110')
        test_student.save()
        test_teacher = User.objects.create_superuser(email='teacher@gmail.com', password='mrrobot990')
        test_teacher.save()
        test_subject = Subject.objects.create(name='subject_1')
        test_subject.save()
        test_course = Course.objects.create(title='Course_1', description='content', teacher=test_teacher,
                                            subject=test_subject, status='online', available_places=20, discount=20,
                                            start_date=date(2023, 1, 10), end_date=date(2023, 1, 30), price=1000)
        test_course.save()
        self.test_new_purchase = {'course': test_course, 'status': 'not_confirmed', 'student': test_student}
        assert self.test_new_purchase

        response = self.client.post('/api/v1/account/login/',
                                    {'email': 'student@gmail.com', 'password': 'neverland110'})
        response_content = json.loads(response.content.decode('utf-8'))
        self.access_token = response_content['access']

    def test_create_purchase(self):
        purchase = Purchase.objects.all()[0]
        response = self.client.create(reverse('purchases-list'), self.test_new_purchase,
                                    HTTP_AUTHORIZATION=f'Bearer {self.access_token}'.format(token))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class DeletePurchaseAPITestCase(APITestCase):
    def setUp(self):
        test_student = User.objects.create_superuser(email='student@gmail.com', password='neverland110')
        test_student.save()
        test_teacher = User.objects.create_superuser(email='teacher@gmail.com', password='mrrobot990')
        test_teacher.save()
        test_subject = Subject.objects.create(name='subject_1')
        test_subject.save()
        test_course = Course.objects.create(title='Course_1', description='content', teacher=test_teacher,
                                            subject=test_subject, status='online', available_places=20, discount=20,
                                            start_date=date(2023, 1, 10), end_date=date(2023, 1, 30), price=1000)
        test_course.save()
        test_purchases = baker.make('purchases.Purchase', course=test_course, student=test_student,
                                    status='not_confirmed', created_at=date.today(), _quantity=5)
        assert test_purchases

        response = self.client.post('/api/v1/account/login/',
                                    {'email': 'student@gmail.com', 'password': 'neverland110'})
        response_content = json.loads(response.content.decode('utf-8'))
        self.access_token = response_content['access']

    def test_delete_course(self):
        purchase = Purchase.objects.all()[0]
        response = self.client.delete(reverse('purchases-detail', args=[purchase.id]),
                                    HTTP_AUTHORIZATION=f'Bearer {self.access_token}'.format(token))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
