from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('degrees/', include('degree.urls')),
    path('courses/', include('courses.urls')),
    path('students/', include('students.urls')),
    path('enrollments/', include('enrollments.urls')),
]