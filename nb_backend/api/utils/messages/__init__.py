"""Messages main module"""

# messages
from .success import SUCCESS
from .error import VALIDATION

def create_message(*args, **kwargs):
    """Create success/error messages.

    Args:
        *args (list): Variable length tuple.
        **kwargs (dict): Variable length dict.
            data (dict): Data to be included in the response
            success (bool): Determines mesg type to be sent, ie. success or error.

    Returns:
        (dict): Response dictionary to be passed to DRF's Response obj.
    """

    msg_key = kwargs.get('msg_key')
    data = kwargs.get('data', [])
    if kwargs.get('success', True):
        status = 'success'
        msg = SUCCESS[msg_key]
    else:
        status = 'error'
        msg = VALIDATION[msg_key]

    return {
        'status': status,
        'message': msg.format(*args),
        'data': data
    }
