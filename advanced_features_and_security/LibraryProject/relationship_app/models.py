from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User
from django.conf import settings

class Author(models.Model):
    name = models.CharField(max_length=200)
=======
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Author(models.Model):
    name = models.CharField(max_length=100)
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length=200)
=======
    name = models.CharField(max_length=100)
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length=200)
=======
    name = models.CharField(max_length=100)
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
<<<<<<< HEAD
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)

    
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

# Create your models here.
=======
    


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f'{self.user.username} - {self.role}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
