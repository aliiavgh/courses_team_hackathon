from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

User = get_user_model()


class Subject(models.Model):
    name = models.SlugField(primary_key=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Subject, self).save(*args, **kwargs)


class Course(models.Model):
    COURSE_STATUS = (
        ('online', 'Online'),
        ('offline', 'Offline')
    )
    title = models.CharField(max_length=180)
    description = models.TextField()
<<<<<<< HEAD
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses', default='default value')
=======
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
>>>>>>> demo
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    status = models.CharField(choices=COURSE_STATUS, max_length=50, null=True)
    address = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=50, default='russian')
    url = models.URLField(max_length=180, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.PositiveIntegerField(validators=[MinValueValidator(5), MaxValueValidator(99)],
                                           blank=True, null=True)
<<<<<<< HEAD
    final_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
=======
    final_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
>>>>>>> demo
    requirements = models.TextField(blank=True, null=True)
    available_places = models.PositiveIntegerField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_available = models.BooleanField()

    def save(self, *args, **kwargs):
        import datetime
<<<<<<< HEAD
        self.is_available = False if (datetime.date.today() >= self.end_date or self.places == 0) else True
=======
        self.is_available = False if (datetime.date.today() > self.end_date or self.available_places == 0) else True
>>>>>>> demo
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class CoursePoster(models.Model):
    image = models.ImageField(upload_to='images/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='posters')
