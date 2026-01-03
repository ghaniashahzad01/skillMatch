from django.urls import path
from .views import employer_dashboard

urlpatterns = [
    path('dashboard/', employer_dashboard, name='employer-dashboard'),
]
