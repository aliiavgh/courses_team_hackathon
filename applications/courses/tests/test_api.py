from datetime import date
from random import randrange

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from model_bakery import baker

from applications.courses.models import Course, Subject
from applications.courses.serializers import CourseSerializer

User = get_user_model()


class CourseAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_teacher = User.objects.create_user(email='teacher@gmail.com', password='mrrobot990')
        cls.test_subject = Subject.objects.create(name='subject_1')
        test_courses = baker.make('courses.Course', teacher=cls.test_teacher,
                                  subject=cls.test_subject, status='online', available_places=20, discount=randrange(99),
                                  start_date=date(2023, 1, 10), end_date=date(2023, 1, 30), price=randrange(100, 50000),
                                  )
        print('>   SetUp data: ', test_courses)
        assert test_courses

    def test_can_read_course_list(self):
        courses = Course.objects.all()
        response = self.client.get(reverse('courses-list'))
        print('>   Response data:', response.data.get('results'))
        serializer_data = CourseSerializer(courses, many=True).data
        print('>   Serializer data: ', serializer_data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data.get('results'), serializer_data)

    def test_can_read_course_detail(self):
        course = Course.objects.get(id=1)
        response = self.client.get(reverse('courses-detail', args=[course.id]))
        serializer_data = CourseSerializer(course).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)





