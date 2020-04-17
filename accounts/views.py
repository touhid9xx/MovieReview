from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from accounts.forms import RegistrationForm


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
       form = RegistrationForm(request.POST or None)
       if form.is_valid():
           user = form.save()
           raw_password = form.cleaned_data['password1']
           user = authenticate(username=user.username, password=raw_password) 
           login(request,user)
           return redirect('index')
       else:
           form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form })    


def login_user(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password'] 


       user = authenticate(username=username,password=password)

       if user is not None:
            if user.is_active:
                login(request,user) 
                return redirect('index')
            else:
                return render(request, 'accounts/login.html',{'error': 'your account has been disabled'})
            
    else:
            return render(request, 'accounts/login.html',{'error': 'Invalid username or password! Try again'})   


            return render(request, 'accounts/login.html')     


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
    else:
        return redirect('login')    