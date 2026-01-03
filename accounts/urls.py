from django.urls import path
from .views import employer_register

urlpatterns = [
    path('register/employer/', employer_register, name='employer-register'),
]
