from django.urls import path, include
from rest_framework import routers
from .views import CourseEnrollmentViewSet, DegreeEnrollmentViewSet

router = routers.DefaultRouter()
router.register(f"api/course-enrollment", CourseEnrollmentViewSet)
router.register(f"api/degree-enrollment", DegreeEnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
