# users/views.py
from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import UserSerializer, UserRegistrationSerializer
import logging

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


logger = logging.getLogger(__name__)

class UserRegistrationView(generics.CreateAPIView):
    # ... (previous code)

    def perform_create(self, serializer):
        user = serializer.save()
        logger.info(f"New user registered: {user.username}")