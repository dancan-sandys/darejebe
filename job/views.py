from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .forms import employeeform, employerForm,vacancyform,applicationform
from .models import Vacancy, Application,Employer,Employee



# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        role = request.POST['account']
        form = UserCreationForm(request.POST)
        role = request.POST.get("role")
        if form.is_valid():
            user = form.save()
            login(request, user)
            print(request.user)
        return redirect(loginpage)
    
    return render(request, 'authentification/signup.html', {"form":form})

def loginpage(request):

    if request.method == "POST":
        role = request.POST['role']
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
        
        else:
        
            message = 'The username or password you entered is incorrect'
            username = request.POST.get("username")
            return render(request, 'authentification/login.html', {"message": message,"username":username})



        if role == 'Employer':
            return redirect(employerprofile)
        else:
            return redirect(applicantprofile)

      
    return render(request, 'authentification/login.html')


def employer(request):
    form = employerForm()
    user = request.user
    if request.method == 'POST':
        form = employerForm(request.POST)
        if form.is_valid():
            new_employer = form.save(commit=False)
            new_employer.user = user
            new_employer.save()


            return redirect(employerprofile)

    return render(request, 'employer/create.html',{'form':form})

def employee(request):
    form = employeeform()
    user = request.user
    if request.method == 'POST':
        form = employeeform(request.POST, request.FILES)
        if form.is_valid():
            new_employee = form.save(commit=False)
            new_employee.user = user
            new_employee.save()
            

            return redirect(applicantprofile)

    return render(request , 'employee/create.html',{"form":form})







def vacancies(request):
    available_vacancies = Vacancy.objects.all()

    return render(request ,'employee/vacancies.html', {"vacancies": available_vacancies})

def applicantprofile(request):
    user = request.user
    try:
        applicant = Employee.objects.get(user = user)
    except:
        return redirect(employee)

    return render( request, 'employee/profile.html', {'profile':applicant})


def employerprofile(request):
    user = request.user

    try:
        profile = Employer.objects.get(user = user)
    except:
        return redirect(employer)

    return render( request, 'employer/profile.html', {'profile':profile})






















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






























