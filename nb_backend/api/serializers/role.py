"""
api/serializers/role.py
role serializer module.
"""

# serializer
from api.serializers.base_serializer import BaseModelSerializer
# models
from api.models.role import Role

# pylint: disable=too-few-public-methods, no-self-use


class RoleSerializer(BaseModelSerializer):
    """Role serializer class."""

    class Meta:
        """Serializer metadata class."""
        model = Role
        fields = '__all__'
