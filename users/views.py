from django.shortcuts import render, redirect, HttpResponse
# from django.contrib.auth import authenticate, login , logout 
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators  import login_required 

# Create your views here.
# @login_required(login_url = 'signin')
def Dashbord (request):
    return render(request, 'users/dashbord.html')

    # return render (request , 'users/home.html')
    
def SignUp(request):
    return render (request , 'users/signup.html')
    # if request.method == 'users/POST':
    #     uname = request.POST.get('name')
    #     email = request.POST.get('email')
    #     pass1 = request.POST.get('password1')
    #     pass2 = request.POST.get('password2')
    #     if pass1 == pass2 :
    #         n_user = User.objects.create_user(username=uname, email=email, password=pass1)
    #         return redirect('signin')
    #     else:
    #         return HttpResponse ("Password not matched")
    # return render(request, 'users/signup.html')

def SignIn(request):
    # return HttpResponse ( "This is sign in page")
    # if request.method == 'users/POST':
    #     uname = request.POST.get('name')
    #     pass1 = request.POST.get('password1')
    #     user = authenticate(request, username=uname, password=pass1)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('home')
    #     else:
    #         error_message = "User not matched!!"
    #         return render(request, 'users/signin.html', {'error_message': error_message})

    return render(request, 'users/signin.html')

def LogOut( request):
    return render (request , 'users/signup.html')
    # logout(request)
    # return redirect ('signin')


def  Profile ( request, username ):
    return render (request , 'users/profile.html')
    # return render( f"Username: {username}" )

def EditProfile(request ,username):
    return render ( request, 'users/editprofile.html')