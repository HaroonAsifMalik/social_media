from django.shortcuts import render , redirect, HttpResponse

# Create your views here.
def create_post (request ,username):
    return render ( request , 'posts/create_post.html')

def post_id( request ,username, id):
    return render (request , 'posts/post_page.html')

def post_comments( request,username ,id):
    return render (request , 'posts/post_comments.html')

def post_likes( request,username ,id):
    return render (request , 'posts/post_likes.html')

def post_shares( request,username ,id):
    return render (request , 'posts/post_shares.html')