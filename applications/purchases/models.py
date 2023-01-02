import uuid

from django.contrib.auth import get_user_model
from django.db import models

from applications.courses.models import Course

User = get_user_model()


class Purchase(models.Model):
<<<<<<< HEAD
=======
    """Buying a course for students"""
>>>>>>> demo
    PURCHASE_STATUS = (
        ('not_confirmed', 'Not confirmed'),
        ('waiting', 'Waiting'),
        ('in_process', 'In process'),
        ('completed', 'Completed')
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='purchases')
<<<<<<< HEAD
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases', default='default value')
    status = models.CharField(choices=PURCHASE_STATUS, max_length=50, default='default value')
=======
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    status = models.CharField(choices=PURCHASE_STATUS, max_length=50, default='not_confirmed')
>>>>>>> demo
    created_at = models.DateTimeField(auto_now_add=True)
    confirmation_code = models.UUIDField(default=uuid.uuid4, blank=True, null=True)
    is_confirm = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student} - {self.status} - {self.course}'

    def save(self, *args, **kwargs):
        import datetime
        if datetime.date.today() >= self.course.end_date and self.is_confirm == True:
            self.status = 'completed'
<<<<<<< HEAD

=======
>>>>>>> demo
