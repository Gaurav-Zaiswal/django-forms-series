from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateField(auto_now=True)
