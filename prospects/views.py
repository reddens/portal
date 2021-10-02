from django.shortcuts import redirect, render
from .models import Student
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def dashboard(request):
    return render('dashboard.html')

@login_required(login_url="/accounts/login/")
def apply(request):
    if request.method == 'POST':
        form = forms.CreateStudent(request.POST, request.FILES)
        if form.is_valid():
            #save student to db
            instance = form.save(commit=False)
            instance.guardian = request.user
            instance.save()
            return redirect('home')

    else: 
        form = forms.CreateStudent()
        return render(request, 'prospects/apply.html', {'form': form})

def dashboard(request):
    students = Student.objects.all().order_by('date')
    return render(request, 'prospects/dashboard.html', {'students':students})

def view_student(request, slug):
    #return HttpResponse(slug)
    student = Student.objects.get(slug=slug)
    return render(request, 'prospects/view_student.html', {'student':student})