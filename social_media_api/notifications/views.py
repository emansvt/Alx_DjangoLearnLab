<<<<<<< HEAD
from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer  # Assume NotificationSerializer is defined

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
