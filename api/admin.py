"""
api/admin.py
api app admin module.
"""

# django
from django.contrib import admin

# models
from api.models.organization import Organization
from api.models.department import Department

admin.site.register(Organization)
admin.site.register(Department)
