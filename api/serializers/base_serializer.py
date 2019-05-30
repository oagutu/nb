"""Dynamic field serializer module"""

# rest_framework
from rest_framework.serializers import ModelSerializer

# pylint: disable=too-few-public-methods


class BaseModelSerializer(ModelSerializer):
    """Base model serializer class."""

    def __init__(self, *args, **kwargs):
        """Serializer intialization method"""

        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

        if fields:
            fields = set(self.fields).difference(fields)
            for field in fields:
                self.fields.pop(field)
