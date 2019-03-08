"""Model helper functions module"""

# rest_framework
from rest_framework import status, exceptions


def get_single_entry(model, primary_key):
    """Get single entry

    Args:
        model (class): Model class to be queried.
        primary_key (uuid): Instance primary key

    Returns:
        (object): Resulting queryset.
    """

    return model.objects.get(pk=primary_key)


def delete_check(request, instance):  # pylint: disable=unused-argument
    """Checks if entry already deleted.

    Args:
        request (object): DRF Request object.
        instance (object): Model instance.

    Raises:
        ValidationError: If entry already deleted.
    """

    if instance.deleted:
        raise exceptions.ValidationError(
            {'status': 'error', 'message': f'Entry - {instance.name} already deleted'},
            status.HTTP_400_BAD_REQUEST)
