from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .forms import employeeform, employerForm,vacancyform,applicationform
from .models import Vacancy, Application,Employer,Employee
from django.contrib.auth.decorators import login_required


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

@login_required(login_url= 'login/')
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

@login_required(login_url= 'login/')
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


@login_required(login_url= 'login/')
def vacancies(request):
    available_vacancies = Vacancy.objects.all()

    return render(request ,'employee/vacancies.html', {"vacancies": available_vacancies})

@login_required(login_url= 'login/')
def applicantprofile(request):
    user = request.user
    try:
        applicant = Employee.objects.get(user = user)
    except:
        return redirect(employee)

    return render( request, 'employee/profile.html', {'profile':applicant})


@login_required(login_url= 'login/')
def employerprofile(request):
    user = request.user

    try:
        profile = Employer.objects.get(user = user)
    except:
        return redirect(employer)

    return render( request, 'employer/profile.html', {'profile':profile})


@login_required(login_url= 'login/')
def employeehome(request):
    return render (request,  'employee/home.html')


@login_required(login_url= 'login/')
def employerhome(request):
    return render (request,  'employer/home.html')


@login_required(login_url= 'login/')
def searchvacancy(request):

    if 'vacancy' in request.GET and request.GET["vacancy"]:
        vacancysearched = request.GET.get('vacancy')
        results = Vacancy.searchvacancy(vacancysearched)

        message = 'The vacancy you searched for is not yet available'

        return render(request, 'employee/vacancysearch.html',{"results":results, "message":message})

    else:
        message = 'The vacancy you searched for is not yet available'

        return render(request, 'employee/vacancysearch.html', {"message":message})

@login_required(login_url= 'login/')
def searchvacancy(request):

    if 'vacancy' in request.GET and request.GET["vacancy"]:
        vacancysearched = request.GET.get('vacancy')
        results = Vacancy.searchvacancy(vacancysearched)

        message = 'The vacancy you searched for is not yet available'

        return render(request, 'employee/vacancysearch.html',{"results":results, "message":message})

    else:
        message = 'The vacancy you searched for is not yet available'

        return render(request, 'employee/vacancysearch.html', {"message":message})


@login_required(login_url= 'login/')
def apply(request, id):
    vacancy = Vacancy.objects.get(id = id)
    user = request.user 
    employer = User.objects.get(username = vacancy.user)
    employer = Employer.objects.get(user = employer)
    new_application = Application(user=user,employer=employer, vacancy=vacancy)
    new_application.save()
    return redirect(applicantprofile)


@login_required(login_url= 'login/')
def applications(request):
    user = request.user
    profile = Employer.objects.get(user = user)
    receivedapplications =Application.objects.filter(employer=profile)
    message = 'You have no applicants so far'

    return render(request, 'employer/applications.html', {"applications":receivedapplications, "message":message})

@login_required(login_url= 'login/')
def vacancy(request):
    form = vacancyform()
    if request.method == 'POST':
        form = vacancyform(request.POST)
        user = request.user
        if form.is_valid():
            new_vacancy = form.save(commit=False)
            new_vacancy.user = user 
            new_vacancy.save()
            
            
            return redirect(landing)

    return render(request, 'employer/addvacancy.html',{"form":form})


@login_required(login_url= 'login/')
def myapplications(request):
    user = request.user 
    Applications = Application.objects.filter(user=user)

    return render(request, 'employee/applications.html', {'applications':Applications})





























