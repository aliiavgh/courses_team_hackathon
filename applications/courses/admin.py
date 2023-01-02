from django.contrib import admin

from applications.courses.models import Course, Subject, CoursePoster


class CoursePosterAdmin(admin.TabularInline):
    model = CoursePoster
    fields = ('image',)
    max_num = 5


class CourseAdmin(admin.ModelAdmin):
    inlines = [CoursePosterAdmin]
<<<<<<< HEAD
    list_display = ['id', 'title', 'likes']

    @staticmethod
    def likes_counter(obj):
        return obj.likes.filter(is_like=True).count()


admin.site.register(Course, CourseAdmin)
admin.site.register(Subject)
admin.site.register(CoursePoster)
=======
    list_display = ['id', 'title']

    """@staticmethod
    def likes_counter(obj):
        return obj.likes.filter(is_like=True).count()"""


admin.site.register(Subject)
admin.site.register(CoursePoster)
admin.site.register(Course, CourseAdmin)
>>>>>>> demo
