from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'useraccounts/signup.html', {'error':'Username already exist'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'useraccounts/signup.html', {'error':'Password Must Match'})
    else:
    
        return render(request, 'useraccounts/signup.html')
    
def login(request):
    return render(request, 'useraccounts/login.html')
    
def logout(request):
    # todo need to route to homepage
    return render(request, 'useraccounts/signup.html')
