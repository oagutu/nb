"""Roles model sub-module"""

# django
from django.db import models

# models
from .base import AuditBaseModel


class Role(AuditBaseModel):
    """Role model class"""

    SA = 'super_admin'
    A = 'admin'
    M = 'moderator'
    U = 'user'
    G = 'guest'

    ROLE_CHOICES = (
        (SA, 'super admin'),
        (A, 'admin'),
        (M, 'moderator'),
        (U, 'user'),
        (G, 'guest')
    )

    role_type = models.CharField(choices=ROLE_CHOICES, unique=True, max_length=20)

    def __repr__(self):
        """Model string representation."""

        return f'<Role: {self.role_type}>'
