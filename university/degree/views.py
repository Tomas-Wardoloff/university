from rest_framework import viewsets
from .serializers import DegreeSerializer
from .models import Degrees


class DegreeViewSet(viewsets.ModelViewSet):
    queryset = Degrees.objects.all()
    serializer_class = DegreeSerializer
