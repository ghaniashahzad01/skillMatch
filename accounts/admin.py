from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_employer', 'is_jobseeker', 'is_staff')
    list_filter = ('is_employer', 'is_jobseeker', 'is_staff')
    search_fields = ('username', 'email')
