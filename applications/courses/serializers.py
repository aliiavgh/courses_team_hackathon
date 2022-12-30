from django.db.models import Avg
from rest_framework import serializers

from applications.courses.models import Course, Subject, CoursePoster


class CoursePosterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoursePoster
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    posters = CoursePosterSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        files_data = request.FILES
        course = Course.objects.create(**validated_data)

        list_images = [CoursePoster(course=course, image=image) for image in files_data.getlist('images')]
        CoursePoster.objects.bulk_create(list_images)
        return course

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['images'] = [image['image'] for image in rep['images']]
        rep['likes'] = instance.likes.filter(is_like=True).count()
        rep['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
        rep['comments'] = instance.comments.all().count()
        rep['already enrolled'] = instance.purchases.filter(is_confirm=True).count()
        return rep


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'

    @staticmethod
    def validate_name(name):
        if Subject.objects.filter(name=name.lower()).exists():
            return serializers.ValidationError('This subject already exists!')
        return name
