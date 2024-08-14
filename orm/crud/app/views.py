from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def create(request):
    # return HttpResponse("success")
    return render(request,'app/register.html')
def register(request):
    #data come from the html to view
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        gender = request.POST['gender']
        contact = request.POST['contactno']
        address = request.POST['address']
        #create object of the model class
        #Insert data into the table
        newuser=person.objects.create(firstname=first_name, lastname=lastname, email=email, gender=gender, contact=contact, address=address)
        # newuser.save()
        print(newuser)
        return HttpResponse("registered successfully")