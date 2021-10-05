from django import forms 
from . import models 

class CreateStudent(forms.ModelForm):
    class Meta: 
        model = models.Student
        fields = ['passport', 'slug']