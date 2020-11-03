from .models import Employee,Employer, Vacancy,Application
from django import forms
from django.contrib.auth.models import User

class employerForm(forms.ModelForm):
    class Meta:
        model = Employer
        exclude = ['user']

class employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['user']


class applicationform(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = '__all__'

class vacancyform(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'