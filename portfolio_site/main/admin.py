from django.contrib import admin

# Register your models here.
from .models import projectModel, blogPosts, aboutExperienceModel

admin.site.register(projectModel)
admin.site.register(blogPosts)
admin.site.register(aboutExperienceModel)