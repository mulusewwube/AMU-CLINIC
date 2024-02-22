from django.db import models




class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name



class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title





class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='about_images/')
   


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctors/images/', blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


        # your_app/models.py






class appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateTimeField()
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name





class Testimonial(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/images/')







