from django.db import models
from django.conf import settings

class EmployerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    company_name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)

    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        default='profile_pics/default.png'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_complete(self):
        return bool(
            self.company_name and
            self.description and
            self.location
        )

    def __str__(self):
        return str(self.user)
