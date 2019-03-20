"""api app tests configuration module"""

# Standard library
import uuid

# 3rd party
import pytest
from rest_framework.test import APIClient

# models
from ..models.organization import Organization

@pytest.fixture(scope='module')
def client():
    """Creates test client."""

    return APIClient()

@pytest.fixture(scope='module')
def gen_uuid():
    """Creates a uuid value.

    Args:
        None

    Returns:
        str: UUID instance.
    """

    return uuid.uuid4()

@pytest.fixture
def org_data():
    """Organization test data.

    Returns:
        dict: Test organizations' data.
    """

    return {
        'testorg': {
            'name': 'TestOrg',
            'description': 'Lorem ipsum ...',
            'domain': 'testorg'
        },
        'testorgtwo': {
            'name': 'TestOrgTwo',
            'description': 'Lorem ipsum ...',
            'domain': 'testorgtwo'
        }
    }

@pytest.fixture
def add_org(org_data):  # pylint: disable=redefined-outer-name
    """Creates Organization instance.

    Args:
        org_list (func): Returns org data.

    Returns:
        obj: Organization model instance.
    """

    org = Organization.objects.create(**org_data['testorgtwo'])
    return org
