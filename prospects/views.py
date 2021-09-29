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
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            #save student to db
            instance = form.save(commit=False)
            instance.guardian = request.user
            instance.save()
            return redirect('home')

        else: 
            form = forms.CreateArticle()
            return render(request, 'prospects/apply.html', {'form': form})