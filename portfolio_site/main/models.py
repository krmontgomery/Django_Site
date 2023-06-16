from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class testModel(models.Model):
    message = models.CharField(("message"), max_length=50)
    def __str__(self):
        return self.message

class blogPosts(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    post_body = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title