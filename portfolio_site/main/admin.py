from django.contrib import admin

# Register your models here.
from .models import testModel, blogPosts

admin.site.register(testModel)
admin.site.register(blogPosts)