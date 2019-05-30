"""Messages main module"""

# 3rd party
from rest_framework import status

# messages
from .success import SUCCESS
from .error import VALIDATION

def create_response(*args, **kwargs):
    """Create success/error responses.

    Args:
        *args (list): Variable length tuple.
        **kwargs (dict): Variable length dict.
            payload (dict): Data to be included in the response
            success (bool): Determines mesg type to be sent, ie. success or error.

    Returns:
        (dict): Response tuple to be passed to DRF's Response obj.
            format => (body, status)
    """

    status_mapper = {
        'created' : status.HTTP_201_CREATED,
        'ok': status.HTTP_200_OK,
        'bad_request': status.HTTP_400_BAD_REQUEST,
        'conflict': status.HTTP_409_CONFLICT,
        'not_found': status.HTTP_404_NOT_FOUND,
    }

    msg_key = kwargs.get('msg_key')

    if kwargs.get('success', True):
        resp_type = 'success'
        msg = SUCCESS[msg_key]
    else:
        resp_type = 'error'
        msg = VALIDATION[msg_key]

    response = {
        'status': resp_type,
        'message': msg.format(*args),
    }

    response.update(kwargs.get('payload', {}))

    return response, status_mapper[kwargs.get('status', 'bad_request')]
