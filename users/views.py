from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout ,get_user_model 
from posts.models import Post 
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from posts.serializers import PostSerializer
# from django.contrib.auth import get_user_model
# from django.contrib.auth.decorators  import login_required 

# Create your views here.
# @login_required(login_url = 'signin')



def Dashboard(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    user= request.user
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'users/dashboard.html', {'post_data': serializer.data , 'user':users})
    
def SignUp(request):
    # return render (request , 'users/signup.html')
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 == pass2 :
            n_user = User.objects.create_user(username=uname, email=email, password=pass1)
            return redirect('signin')
        else:
            return HttpResponse ("Password not matched")
    return render(request, 'users/signup.html')

def SignIn(request):
    # return HttpResponse ( "This is sign in page")
    if request.method == 'POST':
        uname = request.POST.get('name')
        pass1 = request.POST.get('password1')
        user = authenticate(request, username=uname, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = "User not matched!!"
            return render(request, 'users/signin.html', {'error_message': error_message})
    return render(request, 'users/signin.html')

def LogOut( request):
    return render (request , 'users/signup.html')
    # logout(request)
    # return redirect ('signin')


def Profile ( request, username ):
    return render (request , 'users/profile.html')
    # return render( f"Username: {username}" )

def EditProfile(request ,username):
    return render ( request, 'users/editprofile.html')

def Allmessages(request ):
    return render(request , 'users/messaging.html')