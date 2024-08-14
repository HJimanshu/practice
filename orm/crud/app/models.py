from django.db import models

# Create your models here.
class person(models.Model):
    first_name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=20,choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),

    ])
    contact=models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    