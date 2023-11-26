from django.urls import path
from .apiview import *

app_name = 'api_account'

urlpatterns = [
    path('register' , RegisterApiView.as_view() , name='register'),
    path('login' , LogoinApiView.as_view() , name='login'),

    #profile
    path('profile' , ProfileView.as_view() , name='profile'),
    path('profile_update' , ProfileUpdateView.as_view() , name='profile_update'),
]
