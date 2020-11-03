from . import views
from django.urls import path


urlpatterns = [
    path('landing/', views.landing, name = 'landing'),

]