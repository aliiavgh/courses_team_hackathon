from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from applications.courses.models import Course

User = get_user_model()


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', default='0')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='likes')
    is_like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.owner} --> {self.course}'


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    def __str__(self):
        return f'{self.owner} --> {self.course}'


class Bookmark(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='bookmarks')
    is_in_bookmarks = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.owner} --> {self.course}'


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)

    def __str__(self):
        return f'{self.owner} --> {self.course}'
