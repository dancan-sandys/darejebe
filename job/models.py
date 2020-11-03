from django.db import models
import datetime

# Create your models here.
class Vacancy(models.Model):
    position = models.CharField(max_length = 30)
    Description = models.TextField()
    email = models.EmailField()
    


class Employer(models.Model):
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    description = models.TextField()
    email = models.EmailField()

class Employee(models.Model):
    name = models.CharField(max_length = 30)
    qualifications = models.TextField()
    attachments = models.FileField()
    email = models.EmailField()
    phone =models.CharField(max_length = 30)

class Application(models.Model):
    employer = models.ForeignKey(Employer, on_delete = models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete = models.CASCADE)
    Time = models.DateTimeField(auto_now_add =True, blank = True)



