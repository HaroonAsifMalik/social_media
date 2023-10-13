from django.shortcuts import render , redirect , HttpResponse
# Create your views here

def Chat(request , username):
    return render(request , 'messaging/chat.html')