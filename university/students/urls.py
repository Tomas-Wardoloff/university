from django.urls import path, include
from rest_framework import routers
from .views import StudentsViewSet

router = routers.DefaultRouter()
router.register(f"api", StudentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
