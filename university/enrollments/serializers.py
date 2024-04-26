from rest_framework import serializers
from .models import CourseEnrollment, DegreeEnrollment


class CourseEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnrollment
        fields = '__all__'


class DegreeEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DegreeEnrollment
        fields = '__all__'
