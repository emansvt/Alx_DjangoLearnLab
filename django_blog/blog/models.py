from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
<<<<<<< HEAD
    title = models.CharField(max_length=200)  
    content = models.TextField()              
    published_date = models.DateTimeField(auto_now_add=True)  
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
=======
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

 

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
<<<<<<< HEAD
   
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
=======

"Comment(models.Model)", "post", "created_at", "updated_at"
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
