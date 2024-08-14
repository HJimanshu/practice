from django.db import models

# Create your models here.
class Company1(models.Model):
    comapany1_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=200)
    about=models.TextField()
    
    def __str__(self):
        return self.name
    
#Create Employee1 Model here
class Employee1(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=200)
    position=models.CharField(max_length=50,choices=(('it','it'),('not it','not it'),('mobile','mobile'),))  
    
    company=models.ForeignKey(Company1,on_delete=models.CASCADE)
    