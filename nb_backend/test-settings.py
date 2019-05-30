"""Test settings module."""

# pylint: disable=invalid-name, unused-wildcard-import, wildcard-import

from .settings import *

DEBUG = True
TESTING = True

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}
