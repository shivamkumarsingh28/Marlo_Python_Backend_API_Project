from django.urls import path
from .views import Marlo_registerUser, Marlo_user_login, Marlo_user_logout

urlpatterns = [
    path('register/', Marlo_registerUser, name='register'),
    path('login/', Marlo_user_login, name='login'),
    path('logout/', Marlo_user_logout, name='logout'),
]