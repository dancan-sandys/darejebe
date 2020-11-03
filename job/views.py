from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import employeeform, employerForm,vacancyform,applicationform



# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect(accountmanagement)
    
    return render(request, 'authentification/signup.html', {"form":form})

def employer(request):
    form = employerForm()
    if request.method == 'POST':
        form = employerForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(landing)

    return render(request, 'employer/create.html',{'form':form})

def employee(request):
    form = employeeform()
    if request.method == 'POST':
        form = employeeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect(landing)

    return render(request , 'employee/create.html',{"form":form})


def accountmanagement(request):

    if request.method == 'POST':
        accounttype = request.POST['account']
        if accounttype == 'Employer':
            return redirect(employer)
        else:
            return redirect(employee)

    return render(request, 'accountmanagement.html')



def application(request):
    form = applicationform()
    if request.method == 'POST':
        form = applicationform(request.POST)
        if form.is_valid():
            form.save()

            return redirect(landing)

    return render(request, 'employee/apply.html',{"form":form})

def vacancy(request):
    form = vacancyform()
    if request.method == 'POST':
        form = vacancyform(request.POST)
        if form.is_valid():
            form.save()

            return redirect(landing)

    return render(request, 'employer/addvacancy.html',{"form":form})






























