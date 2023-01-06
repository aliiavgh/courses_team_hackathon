from datetime import date
from random import randrange

from django.contrib.auth import get_user_model
from django.test import TestCase
from model_bakery import baker

from applications.courses.models import Subject, Course

User = get_user_model()


class SubjectTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_subject = Subject.objects.create(name='Subject_1')
        test_subject.save()

    def test_subject_lowercase_name(self):
        subject = Subject.objects.get(name='subject_1')
        self.assertTrue(subject.name.islower())


class CourseTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_teacher = User.objects.create_user(email='teacher@gmail.com', password='mrrobot990')
        test_teacher.save()
        test_subject = Subject.objects.create(name='Subject_1')
        test_subject.save()
        test_courses = baker.make('courses.Course', teacher=test_teacher, status='online',
                                  subject=test_subject, available_places=10, discount=20,
                                  start_date=date(2023, 1, 10), end_date=date(2023, 1, 30),
                                  price=1000, _quantity=5)
        assert test_courses

    def test_course_title_max_length(self):
        courses = Course.objects.all()
        title_max_length = courses[0]._meta.get_field('title').max_length
        self.assertEqual(title_max_length, 180)

    def test_course_language_max_length(self):
        course = Course.objects.all()
        language_max_length = course[0]._meta.get_field('language').max_length
        self.assertEqual(language_max_length, 50)

    def test_course_availability(self):
        course = Course.objects.all()
        self.assertTrue(course[0].is_available)

    def test_course_final_price(self):
        course = Course.objects.all()
        self.assertEqual(course[0].final_price, 800)
