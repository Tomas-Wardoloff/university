from rest_framework import viewsets
from .serializers import CourseSerializer
from .models import Courses


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
