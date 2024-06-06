from django.urls import path
from .views import *

urlpatterns = [
    path('', user_login, name='login'),  
    path('register/', register, name='register'),
    path('success/<int:user_id>/', success, name='success'),
    path('login_succssed/<int:user_id>/', login_succssed, name='login_succssed'),
    path('logout/', user_logout, name='logout'),
    path('users/', all_users, name='all_users'),
    path('users/user_info/', user_info, name='user_info')
]