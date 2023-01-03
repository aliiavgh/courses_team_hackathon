from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from applications.feedback.models import Like, Bookmark, Rating
from applications.feedback.serializers import RatingSerializer, BookmarkSerializer


class LikeMixin:

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        like_obj, _ = Like.objects.get_or_create(course_id=pk, owner=request.user)
        like_obj.is_like = not like_obj.is_like
        like_obj.save()
        status_ = 'liked'
        if not like_obj.is_like:
            status_ = 'unliked'
        return Response({'status': status_})


class BookmarkMixin:

    @action(detail=True, methods=['POST'])
    def save_in_bookmarks(self, request, pk=None):
        bookmark_obj, _ = Bookmark.objects.get_or_create(course_id=pk, owner=request.user)
        bookmark_obj.is_in_bookmarks = not bookmark_obj.is_in_bookmarks
        bookmark_obj.save()
        status_ = 'saved in bookmarks'
        if not bookmark_obj.is_in_bookmarks:
            status_ = 'Removed from bookmarks'
        return Response({'status': status_})

    @action(detail=False, methods=['GET'])
    def get_bookmarks(self, request):
        course = Bookmark.objects.filter(is_in_bookmarks=True, owner=request.user)
        list_of_courses = BookmarkSerializer(course, many=True)
        return Response(list_of_courses.data, status=status.HTTP_200_OK)


class RatingMixin:

    @action(detail=True, methods=['POST'])
    def rate(self, request, pk=None):
        RatingSerializer(data=request.data).is_valid(raise_exception=True)
        rating_obj, _ = Rating.objects.get_or_create(course_id=pk, owner=request.user)
        rating_obj.rating = request.data['rating']
        rating_obj.save()
        return Response(request.data, status=status.HTTP_201_CREATED)
