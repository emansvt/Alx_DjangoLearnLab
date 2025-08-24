from django.db import models

<<<<<<< HEAD
=======
# Create your models here.
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
<<<<<<< HEAD
        return f"{self.title} by {self.author} ({self.publication_year})"
=======
        return self.title
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
