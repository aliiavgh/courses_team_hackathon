from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from applications.feedback.models import Comment
from applications.feedback.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
