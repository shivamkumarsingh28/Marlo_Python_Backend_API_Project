from django.urls import path
from .views import Marlo_registerUser, Marlo_user_login, Marlo_user_logout,  MarloProductListView, ApiOverview

urlpatterns = [
    path('', ApiOverview, name='home'),
    path('register/', Marlo_registerUser, name='register'),
    path('product/', MarloProductListView.as_view(), name='snippet-list'),
    path('login/', Marlo_user_login, name='login'),
    path('logout/', Marlo_user_logout, name='logout'),
]
