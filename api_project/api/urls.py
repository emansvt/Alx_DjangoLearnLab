<<<<<<< HEAD
from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api', BookViewSet, basename='api')
urlpatterns = router.urls

=======
from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet 

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
 
 

 
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
