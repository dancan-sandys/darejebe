from . import views
from django.urls import path
from django.conf.urls import url    


urlpatterns = [
    url('^$', views.landing, name = 'landing'),
    url('signup/$', views.signup , name='signup'),
    url('employer/create/$', views.employer, name= 'create_employer'),
    url('employer/addvacancy/$', views.vacancy, name= 'addvacancy'),
    url('employee/apply/$', views.application, name= 'application'),
    url('accounts/select/$', views.accountmanagement, name= 'select'),
    url('employee/create/$', views.employee , name='create_employee')
    
]