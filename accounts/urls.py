from django.urls import path
from .views import employer_register, login_view , logout_view

urlpatterns = [
    path('register/employer/', employer_register, name='employer-register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
