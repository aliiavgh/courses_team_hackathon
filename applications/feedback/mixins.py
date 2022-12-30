from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from applications.feedback.models import Like, Bookmark, Rating
from applications.feedback.serializers import RatingSerializer, BookmarkSerializer


class LikeMixin:

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        like_obj, _ = Like.objects.get_or_create(product_id=pk, owner=request.user)
        like_obj.is_like = not like_obj.is_like
        like_obj.save()
        status_ = 'liked'
        if not like_obj.is_like:
            status_ = 'unliked'
        return Response({'status': status_})


class BookmarkMixin:

    @action(detail=True, methods=['POST'])
    def save_remove_bookmarks(self, request, pk=None):
        bookmark_obj, _ = Bookmark.objects.get_or_create(course_id=pk, owner=request.user)
        bookmark_obj.is_favorite = not bookmark_obj.is_favorite
        bookmark_obj.save()
        status_ = 'saved in bookmarks'
        if not bookmark_obj.is_favorite:
            status_ = 'Removed from bookmarks'
        return Response({'status': status_})

    @action(detail=False, methods=['GET'])
    def get_bookmarks(self, request):
        product = Bookmark.objects.filter(is_favorite=True, owner=request.user)
        product_list = BookmarkSerializer(product, many=True)
        return Response(product_list.data, status=status.HTTP_200_OK)


class RatingMixin:

    @action(detail=True, methods=['POST'])
    def rating(self, request, pk=None):
        RatingSerializer(data=request.data).is_valid(raise_exception=True)
        rating_obj, _ = Rating.objects.get_or_create(product_id=pk, owner=request.user)
        rating_obj.rating = request.data['rating']
        rating_obj.save()
        return Response(request.data, status=status.HTTP_201_CREATED)