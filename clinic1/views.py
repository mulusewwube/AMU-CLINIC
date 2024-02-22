from django.shortcuts import render, redirect
from.models import *

from .models import Contact
from .models import appointment
from .models import Service
from .models import Doctor
from .models import AboutUs







def index(request):
    
    
    return render(request, 'index.html')



def contact_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Save data to the database
        Contact.objects.create(name=name, email=email, subject=subject, message=message)

        # You can also redirect to a success page or render a template



    return render(request, 'contact_form.html')

    return render(request, 'index.html')


def appointment_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        phone = request.POST.get('phone')
        date = request.POST.get('date')
        department = request.POST.get('department')
        doctor = request.POST.get('doctor')
        
        message = request.POST.get('message')

        # Save data to the database
        appointment.objects.create(name=name, email=email, phone=phone, date=date, department=department, doctor=doctor, message=message)




    return render(request, 'appointment_form.html')


def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})
       



def about_us(request):
    about_data = AboutUs.objects.all()
    return render(request, 'clinic1/about_us.html', {'about_data': about_data})
 

def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials.html', {'testimonials': testimonials})








 