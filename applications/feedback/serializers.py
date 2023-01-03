from rest_framework import serializers

from applications.feedback.models import Like, Comment, Bookmark, Rating


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Comment
        fields = '__all__'


class BookmarkSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.title')

    class Meta:
        model = Bookmark
        fields = ('course',)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['course description'] = instance.course.description
        rep['status'] = instance.course.status
        rep['price'] = instance.course.price
        return rep


class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    course = serializers.ReadOnlyField(source='course.title')

    class Meta:
        model = Rating
        fields = '__all__'
