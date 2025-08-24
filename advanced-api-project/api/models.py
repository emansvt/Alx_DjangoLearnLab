from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

<<<<<<< HEAD
=======
    def __str__(self):
        return self.name

>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

<<<<<<< HEAD
#The Author model is created to be associated with multiple books and each Book is linked to an Author through a foreign key, establishing a one-to-many relationship.
=======
    def __str__(self):
        return self.title
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
