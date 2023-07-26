from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class projectModel(models.Model):
    project_title = models.CharField(max_length=200)
    project_image = models.ImageField(upload_to='static/images', height_field=None, width_field=None, max_length=100, default='Project Images')
    image_info = models.TextField(null=True, blank=True)
    project_image_two = models.ImageField(upload_to='static/images', height_field=None, width_field=None, max_length=100, default='Project Images')
    image_info_two = models.TextField(null=True, blank=True)
    project_image_three = models.ImageField(upload_to='static/images', height_field=None, width_field=None, max_length=100, default='Project Images')
    image_info_three = models.TextField(null=True, blank=True)
    project_body = models.TextField(null=True, blank=True)
    project_links = models.URLField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.project_title

class blogPosts(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog_title = models.CharField(max_length=200)
    blog_image = models.ImageField(upload_to='static/images', height_field=None, width_field=None, max_length=100, default='Project Images')
    blog_image_info = models.TextField(null=True, blank=True)
    blog_image_two = models.ImageField(upload_to='static/images', height_field=None, width_field=None, max_length=100, default='Project Images')
    blog_image_info_two = models.TextField(null=True, blank=True)
    blog_image_three = models.ImageField(upload_to='static/images', height_field=None, width_field=None, max_length=100, default='Project Images')
    blog_image_info_three = models.TextField(null=True, blank=True)
    blog_body = models.TextField(null=True, blank=True)
    blog_created_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title