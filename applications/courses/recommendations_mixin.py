from django.db.models import Count, Avg
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from applications.courses.models import Course
from applications.courses.serializers import CourseSerializer


class RecommendationMixin:
    """Выводит топ 5 самых пролайканных курсов"""
    @action(detail=False, methods=['GET'])
    def get_recommended_courses(self, request):
        most_liked_courses = Course.objects.annotate(total_likes=Count('likes')).order_by('likes')[:5]
        courses = CourseSerializer(most_liked_courses, many=True)
        return Response(courses.data, status.HTTP_200_OK)
