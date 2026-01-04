from django.urls import path
from .views import employer_dashboard,employer_profile_view,employer_profile_edit

urlpatterns = [
    path('dashboard/', employer_dashboard, name='employer-dashboard'),
    path('profile/', employer_profile_view, name='employer-profile'),
    path('profile/edit/', employer_profile_edit, name='employer-profile-edit'),
]
