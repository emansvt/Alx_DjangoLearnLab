from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
<<<<<<< HEAD
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        # Create a new UserProfile when a User is created
        UserProfile.objects.create(user=instance)
    else:
        # Save the UserProfile when the User is updated
        instance.userprofile.save()
=======
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
