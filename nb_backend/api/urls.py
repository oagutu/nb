"""
api/urls.py
api url configuration file.
"""

# django
from django.urls import path

# views
from .views.organization import OrganizationView
from .views.organization import OrganizationSingleView

# pylint: disable=invalid-name

urlpatterns = [
    path('organization/', OrganizationView.as_view(), name='organization'),
    path('organization/<uuid:pk>/', OrganizationSingleView.as_view(), name='organization_specific'),
]
