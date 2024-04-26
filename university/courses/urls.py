from django.urls import path, include
from rest_framework import routers
from .views import CourseViewSet

router = routers.DefaultRouter()
router.register(f"api", CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
