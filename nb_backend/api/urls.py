"""
api/urls.py
api url configuration file.
"""

# django
from django.urls import path
from rest_framework.routers import DefaultRouter

# views & viewsets
from api.views.organization import OrganizationView
from api.views.organization import OrganizationSingleView
from api.views.department import DepartmentViewSet
from api.views.role import RoleViewSet

# pylint: disable=invalid-name

router = DefaultRouter()
router.register(r'^department', DepartmentViewSet)
router.register(r'role', RoleViewSet)

urlpatterns = [
    path('organization/', OrganizationView.as_view(), name='organization'),
    path('organization/<uuid:pk>/', OrganizationSingleView.as_view(), name='organization_specific'),
]

urlpatterns += router.urls
