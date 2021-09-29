from django import forms 
from . import models 

class CreateStudent(forms.ModelForm):
    class Meta: 
        model = models.Student
        fields = ['first_name', 'last_name', 'other_name', 'slug', 'thumb']