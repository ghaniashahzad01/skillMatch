from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from .models import EmployerProfile


@receiver(post_save, sender=User)
def create_employer_profile(sender, instance, created, **kwargs):
    if created and instance.is_employer:
        EmployerProfile.objects.create(
            user=instance,
            company_name=instance.username
        )
