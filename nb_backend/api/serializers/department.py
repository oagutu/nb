"""
api/serializers/department.py
Department serializer module.
"""

# rest_framework
from rest_framework import exceptions

# serializer
from api.serializers.base_serializer import BaseModelSerializer
# models
from api.models.department import Department
# utils: helpers
from api.utils.validators.validate_value import check_string
# utils: messages
from api.utils.messages import VALIDATION

# pylint: disable=too-few-public-methods, no-self-use

class DepartmentSerializer(BaseModelSerializer):
    """Department serializer class."""

    class Meta:
        """Serializer metadata class."""
        model = Department
        fields = '__all__'

    def validate_name(self, value):
        """Checks that department name is valid.

        Args:
            self (obj): DepartmentSerializer class instance.
            value (str): Value of the name field to be validated.
        Returns:
            str: Name field value.
        """

        if not check_string(value):
            raise exceptions.ValidationError(VALIDATION['invalid_string'])
        return value
