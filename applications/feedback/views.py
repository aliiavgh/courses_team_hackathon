from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from applications.feedback.models import Comment
from applications.feedback.permissions import IsCommentOwner
from applications.feedback.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
