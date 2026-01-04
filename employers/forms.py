from django import forms
from .models import EmployerProfile


class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = [
            'company_name',
            'description',
            'location',
            'website',
            'profile_picture',
        ]

        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-2 text-gray-100 focus:outline-none focus:border-blue-500'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-2 text-gray-100 focus:outline-none focus:border-blue-500',
                'rows': 4
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-2 text-gray-100 focus:outline-none focus:border-blue-500'
            }),
            'website': forms.URLInput(attrs={
                'class': 'w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-2 text-gray-100 focus:outline-none focus:border-blue-500'
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'text-gray-300'
            }),
        }
