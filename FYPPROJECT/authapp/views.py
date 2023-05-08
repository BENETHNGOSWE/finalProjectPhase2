from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def HomePage(request):
    return render(request, 'FYPAPP/dashboard.html', {})

def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name = request.POST.get('uname')
        password = request.POST.get('pass')
        confirm_password = request.POST.get('confirmpass')

        if password != confirm_password:
            error_msg = 'Password do not match. Please write again'
            return render(request, 'authapp/register.html', {'error_msg':error_msg})

        new_user = User.objects.create_user(name, confirm_password, password)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect('login-page')
  
    return render(request, 'authapp/register.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return HttpResponse('Error, user does not exist')


    return render(request, 'authapp/login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('login-page')

# def test(request):
#     return render(request, 'auth_system/test.html', {})