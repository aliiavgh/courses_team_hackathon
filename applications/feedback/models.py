from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from applications.courses.models import Course

User = get_user_model()


class Like(models.Model):
<<<<<<< HEAD
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', default='default value')
=======
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
>>>>>>> demo
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='likes')
    is_like = models.BooleanField(default=False)


class Comment(models.Model):
<<<<<<< HEAD
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', default='default value')
=======
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
>>>>>>> demo
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()


class Bookmark(models.Model):
<<<<<<< HEAD
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks', default='default value')
=======
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
>>>>>>> demo
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='bookmarks')
    is_in_bookmarks = models.BooleanField(default=False)


class Rating(models.Model):
<<<<<<< HEAD
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings', default='default value')
=======
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
>>>>>>> demo
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

