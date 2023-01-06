import json
import token
from datetime import date
from random import randrange

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client
from rest_framework import status
from rest_framework.test import APITestCase

from model_bakery import baker

from applications.courses.models import Course, Subject
from applications.courses.serializers import CourseSerializer

User = get_user_model()


class ReadCourseAPITestCase(APITestCase):
    def setUp(self):
        test_teacher = User.objects.create_user(email='teacher@gmail.com', password='mrrobot990')
        test_teacher.save()
        test_subject = Subject.objects.create(name='subject_1')
        test_subject.save()
        test_courses = baker.make(
            'courses.Course', title='Course_n', teacher=test_teacher, subject=test_subject,
            status='online', available_places=20, start_date=date(2023, 1, 10), end_date=date(2023, 1, 30),
            price=1000,discount=20, _quantity=5
                                  )
        assert test_courses

    def test_get_course_list(self):
        courses = Course.objects.all()
        response = self.client.get(reverse('courses-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = CourseSerializer(courses, many=True).data
        self.assertEqual(response.data.get('results'), serializer_data)

    def test_get_single_course_detail(self):
        course = Course.objects.all()[0]
        response = self.client.get(reverse('courses-detail', args=[course.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = CourseSerializer(course).data
        self.assertEqual(response.data, serializer_data)


class CreateCourseAPITestCase(APITestCase):
    def setUp(self):
        test_teacher = User.objects.create_superuser(email='teacher@gmail.com', password='mrrobot990')
        test_teacher.save()
        test_subject = Subject.objects.create(name='subject_1')
        test_subject.save()
        self.news_test_course = {
            'title': 'New_course', 'teacher': test_teacher,
            'subject': test_subject, 'available_places': 20, 'description': 'English',
            'status': 'offline', 'start_date': date(2023, 1, 10), 'end_date': date(2023, 1, 30),
            'price': 1000, 'discount': 20,
        }
        response = self.client.post('/api/v1/account/login/',
                                    {'email': 'teacher@gmail.com', 'password': 'mrrobot990'})
        response_content = json.loads(response.content.decode('utf-8'))
        self.access_token = response_content['access']


    def test_create_new_course(self):
        response = self.client.post(reverse('courses-list'), self.news_test_course,
                                   HTTP_AUTHORIZATION=f'Bearer {self.access_token}'.format(token))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class DeleteCourseAPITestCase(APITestCase):
    def setUp(self):
        test_teacher = User.objects.create_superuser(email='teacher@gmail.com', password='mrrobot990')
        test_teacher.save()
        test_subject = Subject.objects.create(name='subject_1')
        test_subject.save()
        test_courses = baker.make(
            'courses.Course', title='Course_n', teacher=test_teacher, subject=test_subject,
            status='online', available_places=20, start_date=date(2023, 1, 10), end_date=date(2023, 1, 30),
            price=1000,discount=20, _quantity=5
                                  )
        assert test_courses

        response = self.client.post('/api/v1/account/login/',
                                    {'email': 'teacher@gmail.com', 'password': 'mrrobot990'})
        response_content = json.loads(response.content.decode('utf-8'))
        self.access_token = response_content['access']

    def test_delete_course(self):
        course = Course.objects.all()[0]
        response = self.client.delete(reverse('courses-detail', args=[course.id]),
                                    HTTP_AUTHORIZATION=f'Bearer {self.access_token}'.format(token))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthorized_user_deletes_course(self):
        course = Course.objects.all()[0]
        response = self.client.delete(reverse('courses-detail', args=[course.id]),)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
