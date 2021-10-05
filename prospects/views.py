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
            instance.first_name = request.POST.get('first_name')
            instance.last_name = request.POST.get('last_name')
            instance.other_name = request.POST.get('other_name')
            instance.dob = request.POST.get('dob')
            instance.state_of_origin = request.POST.get('state_of_origin')
            instance.previous = request.POST.get('previous')
            instance.medical = request.POST.get('medical')
            instance.qualification = request.POST.get('qualification')
            instance.reason = request.POST.get('reason')
            instance.class_seeked = request.POST.get('class_seeked')
            instance.guardian = request.user
            instance.guardian_fname = request.POST.get('guardian_fname')
            instance.guardian_address = request.POST.get('guardian_address')
            instance.guardian_state = request.POST.get('guardian_state')
            instance.guardian_lga = request.POST.get('guardian_lga')
            instance.responsible_party = request.POST.get('responsible_party')
            instance.doctor = request.POST.get('doctor')
            instance.phone = request.POST.get('phone')
            instance.status = "Application Pending"
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