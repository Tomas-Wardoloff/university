from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Students


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
