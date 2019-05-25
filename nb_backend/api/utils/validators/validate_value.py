"""Validate general values module."""

# std. library
import re

def check_string(value):
    """Checks for valid string.

    Args:
        value (str): String value to be validated.

    Returns:
        Bool: True if valid string
    """

    return re.match(r'^([a-z])+([-_/.&\s])*([a-z])+$', value.lower())
