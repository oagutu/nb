"""
api/admin.py
api app admin module.
"""

# django
from django.contrib import admin

# models
from .models.organization import Organization

admin.site.register(Organization)
