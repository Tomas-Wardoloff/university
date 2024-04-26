from django.urls import path, include
from rest_framework import routers
from .views import DegreeViewSet

router = routers.DefaultRouter()
router.register(f"api", DegreeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
