from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
=======
    author = serializers.ReadOnlyField(source='author.username')

>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
=======
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.ReadOnlyField(source='post.id')

>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
