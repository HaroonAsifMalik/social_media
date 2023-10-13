from django.urls import path , include
from . import views

app_name='messaging'
urlpatterns = [
    path('',views.Chat , name='chat'),
]