<<<<<<< HEAD
from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView
=======
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
<<<<<<< HEAD
router.register(r'feed', FeedView, basename='user-feed')

urlpatterns = [
    path('feed/', FeedView.as_view(), name='user-feed'),
    path('', include(router.urls)),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike-post'),
    path('posts/<int:pk>/like/', like_post, name='like-post'),
]
=======

urlpatterns = router.urls
"feed/"
"<int:pk>/like/", "<int:pk>/unlike/"
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
