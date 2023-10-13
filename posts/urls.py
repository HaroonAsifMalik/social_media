from django.urls import path , include
from . import views
"""
Create Post: /post/create/
Post Detail: /post/<post_id>/
Comment on Post: /post/<post_id>/comment/
Like Post: /post/<post_id>/like/
Share Post: /post/<post_id>/share/
"""
app_name = 'posts'

urlpatterns =[
    path('create/', views.create_post, name='create_post'),
    path( '<int:id>/' , views.post_id , name='post_id' ),
    path( '<int:id>/comments/' , views.post_comments , name='post_comments' ),
    path( '<int:id>/likes/' , views.post_likes , name='post_likes' ),
    path( '<int:id>/shares/' , views.post_shares, name='post_shares' ),
]