from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from applications.courses.models import Course


class Like(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='likes')
    is_like = models.BooleanField(default=False)


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()


class Bookmark(models.Model): #<=> Favorites
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='bookmarks')
    is_in_bookmarks = models.BooleanField(default=False)


class Rating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

