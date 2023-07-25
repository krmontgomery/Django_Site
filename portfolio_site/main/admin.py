from django.contrib import admin

# Register your models here.
from .models import projectModel, blogPosts

admin.site.register(projectModel)
admin.site.register(blogPosts)