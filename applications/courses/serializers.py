from rest_framework import serializers

from applications.courses.models import Image, Course, Subject


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        files_data = request.FILES
        course = Course.objects.create(**validated_data)

        list_images = [Image(course=course, image=image) for image in files_data.getlist('images')]
        Image.objects.bulk_create(list_images)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['images'] = [image['image'] for image in rep['images']]
        return rep


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'

    def validate_name(self, name):
        if Subject.objects.filter(name=name.lower()).exists():
            return serializers.ValidationError('This subject already exists!')
        return name
