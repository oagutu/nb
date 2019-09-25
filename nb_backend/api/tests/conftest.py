"""api app tests configuration module"""

# Standard library
import uuid

# 3rd party
import pytest
from rest_framework.test import APIClient

# models
from api.models.organization import Organization
from api.models.department import Department
from api.models.role import Role

# pylint: disable=redefined-outer-name


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
def add_org(org_data):
    """Creates Organization instance.

    Args:
        org_data (func): Returns org data.

    Returns:
        obj: Organization model instance.
    """

    org = Organization.objects.create(**org_data['testorgtwo'])
    return org


@pytest.fixture
def dept_data(add_org):
    """Department test data.

    Args:
        add_org (obj): Organization obj fixture.

    Returns:
        dict: Test department data.
    """
    return {
        'test_dept': {
            'name': 'TestDept',
            'description': 'Test department',
            'organization': str(add_org.id)
        }
    }


@pytest.fixture
def add_dept(dept_data, add_org):
    """Creates Department instance.

    Args:
        dept_data (func): Returns org data.
        add_org (func): Organization obj fixture.

    Returns:
        obj: Department model instance.
    """
    data = dept_data['test_dept']
    data.update({'organization': add_org})

    return Department.objects.create(**data)


@pytest.fixture
def add_role():
    """Creates Role instance.

    Returns:
        obj: Role model instance.
    """

    return Role.objects.create(role_type='user')

