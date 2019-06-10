"""
api/models/department.py
Department model module
"""

# django
from django.db import models

# models
from api.models.base import AuditBaseModel
from api.models.organization import Organization

# pylint: disable=too-few-public-methods


class Department(AuditBaseModel):
    """Department model class."""

    name = models.CharField(max_length=40)
    description = models.CharField(max_length=140, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
