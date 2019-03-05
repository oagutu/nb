"""
api/models/base.py
Model base module.
"""

# in-built
import uuid

# django
from django.db import models
from django.utils import timezone

class Base(models.Model):
    """Main api model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        """Base model metadata class"""

        abstract = True


class AuditBaseModel(Base):
    """Audit class"""

    created_by = models.UUIDField(null=True)
    created_on = models.DateTimeField(default=timezone.now())
    edited_by = models.UUIDField(null=True)
    edited_on = models.DateTimeField(null=True)
    deleted_by = models.UUIDField(null=True)
    deleted_on = models.DateTimeField(null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        """Audit model metadata class"""

        abstract = True
