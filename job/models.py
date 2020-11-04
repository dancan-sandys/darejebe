from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Vacancy(models.Model):
    position = models.CharField(max_length = 30)
    Description = models.TextField()
    email = models.EmailField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    @classmethod
    def searchvacancy(cls, position):
        vacancies = cls.objects.filter(position = position)

        return vacancies
    


class Employer(models.Model):
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    description = models.TextField()
    email = models.EmailField()
    website = models.URLField(max_length = 255)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    

class Employee(models.Model):
    name = models.CharField(max_length = 30)
    qualifications = models.TextField()
    attachments = models.FileField()
    email = models.EmailField()
    phone =models.CharField(max_length = 30)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

class Application(models.Model):
    employer = models.ForeignKey(Employer, on_delete = models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete = models.CASCADE)
    Time = models.DateTimeField(auto_now_add =True, blank = True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)



