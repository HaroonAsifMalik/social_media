from django.contrib import admin
from django.urls import path , include 
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views  # ----

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


    #reset passwords URLs ------------------
    ###This is Build-in View which is render by default --- user submit email for reset
    path ( 'reset_password/' , auth_views.PasswordResetView.as_view(), name='reset_password'),
    ###The email sent message
    path('reset_password_sent/' , auth_views.PasswordResetDoneView.as_view() , name='password_reset_done'),
    ###To show the conformation msg
    path('reset/<uidb64>/<token>' , auth_views.PasswordResetConfirmView.as_view() , name='password_reset_confirm'),
    
    path( 'reset_password_complete/' , auth_views.PasswordResetCompleteView.as_view() , name="password_reset_complete" )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)