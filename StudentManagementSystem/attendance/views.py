# attendance/views.py
from rest_framework import generics, permissions
from .models import Attendance
from .serializers import AttendanceSerializer
import logging


class AttendanceListCreateView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (permissions.IsAuthenticated,)

class AttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (permissions.IsAuthenticated,)

logger = logging.getLogger(__name__)

class AttendanceListCreateView(generics.ListCreateAPIView):
    # ... (previous code)

    def perform_create(self, serializer):
        attendance = serializer.save()
        logger.info(f"Attendance marked: {attendance.student} {'present' if attendance.status else 'absent'} in {attendance.course} on {attendance.date}")

        