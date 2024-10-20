from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),  
    path('logout/', logout_view, name='logout'),
    path('my-profile/', my_profile, name='my_profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    ]
