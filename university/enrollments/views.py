from rest_framework import viewsets
from .serializers import CourseEnrollmentSerializer, DegreeEnrollmentSerializer
from .models import CourseEnrollment, DegreeEnrollment


class CourseEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = CourseEnrollment.objects.all()
    serializer_class = CourseEnrollmentSerializer


class DegreeEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = DegreeEnrollment.objects.all()
    serializer_class = DegreeEnrollmentSerializer
