from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class projectModel(models.Model):
    project_title = models.CharField(max_length=200)
    project_images = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default='Project Images')
    project_body = models.TextField(null=True, blank=True)
    project_links = models.URLField(max_length=200)
    def __str__(self):
        return self.project_title

class blogPosts(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    post_body = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title