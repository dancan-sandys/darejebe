from django.contrib import admin
from .models import Employee,Employer,Vacancy,Application
# Register your models here.

admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(Vacancy)
admin.site.register(Application)
