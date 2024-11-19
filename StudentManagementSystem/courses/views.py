# courses/views.py
from rest_framework import generics, permissions
from .models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import logging

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticated,)

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticated,)

class EnrollmentListCreateView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CourseListCreateView(generics.ListCreateAPIView):
    # ... (previous code)

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
logger = logging.getLogger(__name__)

class EnrollmentListCreateView(generics.ListCreateAPIView):
    # ... (previous code)

    def perform_create(self, serializer):
        enrollment = serializer.save()
        logger.info(f"New enrollment: {enrollment.student} enrolled in {enrollment.course}")


