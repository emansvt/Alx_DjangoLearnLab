from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    class Roles(models.TextChoices):
        ADMIN = 'Admin', 'Admin'
        LIBRARIAN = 'Librarian', 'Librarian'
        MEMBER = 'Member', 'Member'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.MEMBER)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
 
    if created:
        UserProfile.objects.create(user=instance)
    else:

        UserProfile.objects.get_or_create(user=instance)
