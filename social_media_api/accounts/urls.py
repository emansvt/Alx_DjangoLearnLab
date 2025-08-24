from django.urls import path
<<<<<<< HEAD
from .views import UserRegistrationView, UserLoginView, UserProfileView, follow_user, unfollow_user

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
]
=======
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/', include('posts.urls')),
    "unfollow/<int:user_id>/", "follow/<int:user_id>"
]
 
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
