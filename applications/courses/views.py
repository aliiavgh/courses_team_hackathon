from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from applications.courses.models import Course, Subject
from applications.courses.serializers import CourseSerializer, SubjectSerializer
from applications.feedback.mixins import LikeMixin, BookmarkMixin, RatingMixin


@method_decorator(cache_page(60*60), name='dispatch')
class CourseViewSet(LikeMixin, BookmarkMixin, RatingMixin, ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['subject', 'price', 'start_date']
    search_fields = ['title', 'description']
    ordering_fields = ['price']

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class SubjectViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
