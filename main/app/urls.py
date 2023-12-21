from django.contrib.auth.views import LogoutView
from django.urls import path

from app.views import *




urlpatterns = [
    path('', index, name='index'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', my_logout, name='logout'),
    path('create_offer/', CreateOffer.as_view(), name='create_offer'),
]
