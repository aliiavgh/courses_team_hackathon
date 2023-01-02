from rest_framework import serializers

from applications.feedback.models import Like, Comment, Bookmark, Rating


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(required=False)

    class Meta:
        model = Comment
        fields = '__all__'


class BookmarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookmark
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    course = serializers.ReadOnlyField(source='course.title')

    class Meta:
        model = Rating
        fields = '__all__'
