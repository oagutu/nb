"""
api/serializers/organization.py
Organization model serializer module.
"""

# rest_framework
from rest_framework import serializers

# models
from ..models.organization import Organization

class OrganizationSerializer(serializers.ModelSerializer):
    """Organization model serializer class."""

    # edited_on = serializers.DateTimeField(allow_null=True)

    class Meta:
        """Serializer metadat class."""
        model = Organization
        fields = '__all__'
