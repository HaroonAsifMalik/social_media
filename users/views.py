from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout ,get_user_model 
from posts.models import Post 
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from posts.serializers import PostSerializer 
from .serializers import UserSerializer 
from messaging.models import Conversation ,Message 
from rest_framework.decorators import api_view
from rest_framework.response import Response


def Dashboard(request):
    posts = Post.objects.all()
    ps_serializer = PostSerializer(posts, many=True)

    User = get_user_model()
    users = User.objects.all()
    us_serializer = UserSerializer(users, many=True)

    user = request.user  # Get the currently logged-in user
    print ( ps_serializer)
    return render(request, 'users/dashboard.html', {'post_data': ps_serializer.data, 'users': us_serializer.data, 'profile_name': user.username})
    
def SignUp(request):
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
    logout(request)
    return redirect('signin')

@api_view(['GET'])
def current_user_profile(request):
    if request.user.is_authenticated:
        u_id= request.user.id
        user_posts = Post.objects.filter(author_id=u_id)
        serializer = PostSerializer( user_posts, many=True)
        print ( serializer)
        # return Response(serializer.data)
        return render(request , 'users/profile.html' , {'post_data':serializer.data})
    else:
        return Response({"detail": "User is not authenticated."})


# @api_view(['PATCH'])
def editprofile(request):
    return render(request , 'users/editprofile.html')
#     data = request.data
#     user = request.user  # Get the current user
#     print(data.author)
#     # Update the user's username
#     if 'username' in data:
#         user.username = data['username']
#         user.save()
#         serializer = UserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)

def Allmessages(request ):
    conversations = Conversation.objects.all()
    # print ( conversations)
    # Get unique participants' usernames
    participant_usernames = set()
    for conversation in conversations:
        for participant in conversation.participants.all():
            if participant != request.user and participant.username != 'admin' :  # Exclude the current user
                participant_usernames.add(participant.username)

    # print (participant_usernames)
    
    return JsonResponse(list(participant_usernames), safe=False)
