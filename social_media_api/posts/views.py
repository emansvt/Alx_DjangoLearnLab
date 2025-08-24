<<<<<<< HEAD
from rest_framework import viewsets, permissions, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from notifications.models import Notification
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, viewsets


=======
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
<<<<<<< HEAD
    permission_classes = [permissions.IsAuthenticated]

    def get_post(self, pk):
        return generics.get_object_or_404(Post, pk=pk)
=======
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
<<<<<<< HEAD
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

User = get_user_model()

class UserFeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer 

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all() 
        return Post.objects.filter(author__in=following_users).order_by('-created_at') 
    
    @api_view(['POST'])
@permissions.IsAuthenticated
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk) 
    
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    
    if created:
        Notification.objects.create(
            recipient=post.author, 
            actor=request.user,
            verb='liked your post',
            target=post
        )
        return Response({"message": "Post liked."}, status=201)
    
    return Response({"message": "You already liked this post."}, status=400)

@api_view(['POST'])
@permissions.IsAuthenticated
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({"message": "Post unliked."}, status=204)
    except Like.DoesNotExist:
        return Response({"message": "You haven't liked this post."}, status=400)
=======
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    "Post.objects.filter(author__in=following_users).order_by", "following.all()"
    "generics.get_object_or_404(Post, pk=pk)", "Like.objects.get_or_create(user=request.user, post=post)", "Notification.objects.create"
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
