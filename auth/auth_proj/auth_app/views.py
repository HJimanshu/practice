from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            print(user)
            login(request, user)
            return 'success'
    else:
       initial_data={'username':'', 'email':'','password1':'','password2':'',} 
       form=UserCreationForm(initial=initial_data)
    return render(request,'auth/register.html',{'form':form})
            
  
def login_view(request):
    pass
def dashboard_view(request):    
    pass
def logout_view(request):
    pass