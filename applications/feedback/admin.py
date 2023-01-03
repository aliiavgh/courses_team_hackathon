from django.contrib import admin

from applications.feedback.models import Like, Comment, Bookmark, Rating

admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Bookmark)
admin.site.register(Rating)

