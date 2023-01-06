from django.contrib import admin

from applications.courses.models import Course, Subject

admin.site.register(Course)
admin.site.register(Subject)

