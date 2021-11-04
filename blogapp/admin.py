from django.contrib import admin
from .models import Blog, CommentModel

# Register your models here.
admin.site.register(Blog)
admin.site.register(CommentModel)