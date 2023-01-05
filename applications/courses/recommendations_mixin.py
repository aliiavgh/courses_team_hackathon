from django.db.models import Count, Avg
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from applications.courses.models import Course
from applications.courses.serializers import CourseSerializer
from applications.feedback.models import Like, Bookmark, Rating
from applications.feedback.serializers import RatingSerializer, BookmarkSerializer


class RecommendationMixin:
    @action(detail=False, methods=['GET'])
    def get_recommended_courses(self, request):
        most_rated_courses = Course.objects.annotate(rating=Avg('ratings')).order_by('ratings')[:10]
        courses = CourseSerializer(most_rated_courses, many=True)
        return Response(courses.data, status.HTTP_200_OK)

