from django.contrib import admin

# Register your models here.
from .models import homeModel, projectModel, blogPosts, aboutModel, aboutExperienceModel

admin.site.register(homeModel)
admin.site.register(projectModel)
admin.site.register(blogPosts)
admin.site.register(aboutModel)
admin.site.register(aboutExperienceModel)