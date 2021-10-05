from django.db import models
from django.db.models.fields import TextField 
from django.contrib.auth.models import User 

# Create your models here
class Student(models.Model):
    slug = models.SlugField()
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    other_name = models.CharField(max_length=100, null=True)
    previous = models.CharField(max_length=100, null=True)
    dob = models.DateTimeField(auto_now_add=False, null=True)
    state_of_origin = models.CharField(max_length=100, null=True)
    medical = models.CharField(max_length=100, null=True)
    qualification = models.CharField(max_length=100, null=True)
    reason = models.CharField(max_length=1000, null=True)
    class_seeked = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    passport = models.ImageField(default="default.jpg", blank=True)
    guardian = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)
    guardian_fname = models.CharField(max_length=100, null=True)
    guardian_address = models.CharField(max_length=100, null=True)
    guardian_state = models.CharField(max_length=100, null=True)
    guardian_lga = models.CharField(max_length=100, null=True)
    responsible_party = models.CharField(max_length=100, null=True)
    doctor = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.first_name + self.last_name + " -" + self.status
