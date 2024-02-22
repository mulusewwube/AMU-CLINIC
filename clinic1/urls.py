from django.urls import path


from django.urls import include
from . import views

from .views import contact_form,appointment_form
from .views import service_list, doctor_list, about_us,testimonials






urlpatterns = [

path('', views.index, name='index'),


path('contact/', contact_form, name='contact_form'),
path('appointment/', appointment_form, name='appointment_form'),
  
path('services/', service_list, name='service_list'),
path('doctors/', doctor_list, name='doctor_list'),
path('about/', views.AboutUs, name='AboutUs'),

 path('testimonials/', testimonials, name='testimonials'),
   

  ]