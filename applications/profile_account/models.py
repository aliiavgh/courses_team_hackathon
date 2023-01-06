from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

User = get_user_model()


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)


class Profile(AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20)
    educations = models.TextField()
    language = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email