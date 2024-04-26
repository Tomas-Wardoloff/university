from rest_framework import serializers
from .models import Degrees


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degrees
        fields = '__all__'
