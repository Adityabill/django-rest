from django.db import models

# Create your models here.
class employees(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    time_stamp = models.DateTimeField(auto_now_add=True)
