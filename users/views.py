from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login , logout 
from django.contrib.auth.models import User
from django.contrib.auth.decorators  import login_required 

# Create your views here.
@login_required(login_url = 'signin')
def HomePage (request):
    return render (request , 'home.html')
    
def SignUp(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 == pass2 :
            n_user = User.objects.create_user(username=uname, email=email, password=pass1)
            return redirect('signin')
        else:
            return HttpResponse ("Password not matched")

    return render(request, 'signup.html')

def SignIn(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        pass1 = request.POST.get('password1')
        user = authenticate(request, username=uname, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('User not matched!!')

    return render(request, 'signin.html')

def SignOut( request):
    logout(request)
    return redirect ('signin')