from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class projectModel(models.Model):
    project_title = models.CharField(max_length=200)
    project_image = models.ImageField(upload_to='static/images', blank=True, null=True, height_field=None, width_field=None, max_length=100,)
    image_info = models.TextField(null=True, blank=True)
    project_image_two = models.ImageField(upload_to='static/images', blank=True, null=True, height_field=None, width_field=None, max_length=100,)
    image_info_two = models.TextField(null=True, blank=True)
    project_image_three = models.ImageField(upload_to='static/images', blank=True, null=True, height_field=None, width_field=None, max_length=100,)
    image_info_three = models.TextField(null=True, blank=True)
    project_body = models.TextField(null=True, blank=True)
    project_links = models.URLField(max_length=500, null=True, blank=True)
    project_links_two = models.URLField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.project_title

class blogPosts(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog_title = models.CharField(max_length=200)
    blog_image = models.ImageField(upload_to='static/images', blank=True, null=True, height_field=None, width_field=None, max_length=100,)
    blog_image_info = models.TextField(null=True, blank=True)
    blog_body = models.TextField(null=True, blank=True)
    blog_created_date = models.DateTimeField(auto_now=True)
    blog_topic_one_title = models.CharField(max_length=200, default='Default')
    blog_topic_image_one = models.ImageField(upload_to='static/images', blank=True, null=True, height_field=None, width_field=None, max_length=100,)
    blog_topic_image_info = models.TextField(null=True, blank=True)
    topic_one_body = models.TextField(null=True, blank=True)
    blog_topic_two_title = models.CharField(max_length=200, default='Default')
    blog_topic_image_two = models.ImageField(upload_to='static/images', blank=True, null=True, height_field=None, width_field=None, max_length=100,)
    blog_topic_image_info_two = models.TextField(null=True, blank=True)
    topic_one_body_two = models.TextField(null=True, blank=True)
    blog_links = models.URLField(max_length=500, null=True, blank=True)
    blog_links_two = models.URLField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.blog_title
    
class aboutModel(models.Model):
    about_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    about_body = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.about_name

class aboutExperienceModel(models.Model):
    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    job_description = models.TextField(null=True, blank=True)
    tech_list = (
        ('RPGLE', 'RPGLE'), 
        ('CL','CL'),
        ('DB2','DB2'), 
        ('SQL','SQL'), 
        ('Python','Python'), 
        ('Node.js', 'Node.js'),
        ('Javascript','Javascript'),
        ('HTML','HTML'), 
        ('CSS','CSS')
        )
    tech_used = models.CharField(null=True, blank=True, max_length=32, choices=tech_list)
    tech_used_two = models.CharField(null=True, blank=True, max_length=32, choices=tech_list)
    tech_used_three = models.CharField(null=True, blank=True, max_length=32, choices=tech_list)
    tech_used_four = models.CharField(null=True, blank=True, max_length=32, choices=tech_list)
    tech_used_five = models.CharField(null=True, blank=True, max_length=32, choices=tech_list)
    def __str__(self):
        return self.job_title
    