from . import views
from django.urls import path
from django.conf.urls import url    


urlpatterns = [
    url('^$', views.landing, name = 'landing'),
    url('signup/$', views.signup , name='signup'),
    url('employer/create/$', views.employer, name= 'create_employer'),
    url('employer/addvacancy/$', views.vacancy, name= 'addvacancy'),
    url('employee/apply/$', views.application, name= 'application'),
    url('employee/create/$', views.employee , name='create_employee'),
    url('vacancies/$', views.vacancies, name='vacancies'),
    url('employee/profile/$', views.applicantprofile, name='applicantprofile'),
    url('employer/profile/$', views.employerprofile, name='employerprofile'),
    url('login/$', views.loginpage, name='login'),
    url('employee/home/$', views.employeehome, name= 'employeehome' ),
    url('employer/home/$', views.employerhome, name= 'employerhome' ),
    url('search/vacancy/$', views.searchvacancy, name='searchvacancy')
]