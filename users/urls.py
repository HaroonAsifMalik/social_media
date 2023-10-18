from django.contrib import admin
from django.urls import path , include 
from . import views
from django.conf import settings
from django.conf.urls.static import static

# app_name = "users"
urlpatterns = [
    path( '', views.SignIn , name='signin'),
    path( 'dashboard/' , views.Dashboard, name='dashboard' ),
    path( 'signup/' , views.SignUp , name='signup'),
    path('logout/' , views.LogOut , name='logout'),
    path('profile/', views.current_user_profile, name='current_user_profile'), # we can access profile by current user, 

    #To access posts apps urls
    path('profile/<str:username>/post/', include('posts.urls', namespace='posts')),
    
    #URLs with username Ex:profile/ali/edit
    path('profile/edit/', views.editprofile , name='editprofile'),

    #URLs messaging apps
    path('messages/',views.Allmessages , name='allmessages'),
    path('messages/<str:username>',include('messaging.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)