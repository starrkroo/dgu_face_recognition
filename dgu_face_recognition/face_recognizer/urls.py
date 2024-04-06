from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', verify_face),
    path('register_account', register_face)
]
