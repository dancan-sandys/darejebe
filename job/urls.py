from . import views
from django.urls import path
from django.conf.urls import url    


urlpatterns = [
    url('^$', views.landing, name = 'landing'),
    url('signup/$', views.signup , name='signup'),
    url('employer/create/$', views.employer, name= 'create_employer'),
    url('employer/addvacancy/$', views.vacancy, name= 'addvacancy'),
    url('employee/appy/$', views.application, name= 'application')
]