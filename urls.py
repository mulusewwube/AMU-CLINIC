"""
URL configuration for clinic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import include
from django.conf import settings





from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('clinic1/', include('clinic1.urls')),
    path('', include('clinic1.urls')),
    path('index/', include('clinic1.urls')),

    path('contact_form/', include('clinic1.urls')),
    path('appointment_form/', include('clinic1.urls')),

    path('Services/', include('clinic1.urls')),

    path('doctors/', include('clinic1.urls')),

    path('about/', include('clinic1.urls')),
    path('testimonials/', testimonials, name='testimonials'),



   


   

]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)