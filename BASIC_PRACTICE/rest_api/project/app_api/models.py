from django.db import models

# Create your models here.
class Company(models.Model):
    Company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length= 50, choices=(('it','it'),('Mobile','Mobile'),('non It ', 'Non It')))
    def __str__(self):
        return self.name
#create Employee model
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    position = models.CharField(max_length= 50, choices=(('senior developer','sd'),('junior developer','jd'),('manager','manager')))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    
    