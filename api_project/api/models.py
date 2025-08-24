from django.db import models

class Book(models.Model):
<<<<<<< HEAD
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
=======
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
 
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
