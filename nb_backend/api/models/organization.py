"""
api/models/organization.py
Organization model module
"""

# django
from django.db import models

# models
from .base import AuditBaseModel

class Organization(AuditBaseModel):
    """Organization model class."""

    name = models.CharField(max_length=40)
    description = models.CharField(max_length=140, null=True, blank=True)
    domain = models.CharField(max_length=30)
