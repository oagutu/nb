"""Model helper functions module"""

# rest_framework
from rest_framework import status, exceptions

# utils
from api.utils.messages import VALIDATION

# pylint: disable=protected-access

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
            {'status': 'error', 'message': VALIDATION['already_deleted'].format(instance.name)},
            status.HTTP_400_BAD_REQUEST)

def entry_exists(model, primary_key):
    """Checks if an entry exists in the database.

    Args:
        model (class): Model class to be queried.
        primary_key (uuid): Instance primary key

    Returns:
        (object): Resulting queryset if object exists else raises exception
    """

    try:
        return get_single_entry(model, primary_key)
    except model.DoesNotExist:
        raise exceptions.NotFound(
            {
                'status': 'error',
                'message': VALIDATION['not_found'].format(model._meta.object_name, primary_key)},
            status.HTTP_404_NOT_FOUND
        )

# TODO: replace "get_single_entry" func with "entry_exists" func
