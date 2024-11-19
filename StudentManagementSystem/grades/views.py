# grades/views.py
from rest_framework import generics, permissions
from .models import Grade
from .serializers import GradeSerializer
import logging


class GradeListCreateView(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (permissions.IsAuthenticated,)

class GradeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (permissions.IsAuthenticated,)


logger = logging.getLogger(__name__)

class GradeListCreateView(generics.ListCreateAPIView):
    # ... (previous code)

    def perform_create(self, serializer):
        grade = serializer.save()
        logger.info(f"New grade added: {grade.student} received {grade.grade} in {grade.course}")

