from django.urls import path, include
from .views import register,index,log_in_user,log_out_user

urlpatterns = [
    path('index',index,name='index'),
    path('register',register,name='register'),
    path('login',log_in_user,name='login'),
    path('logout',log_out_user,name='logout'),

]