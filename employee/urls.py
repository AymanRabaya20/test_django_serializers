from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet, 'employee')

urlpatterns = [
    path("", include(router.urls))
]
