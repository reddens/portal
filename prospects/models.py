from django.db import models
from django.db.models.fields import TextField 
from django.contrib.auth.models import User 

# Create your models here
class Student(models.Model):
    slug = models.SlugField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default="default.jpg", blank=True)
    guardian = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name + self.last_name
