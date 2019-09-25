"""Roles test module."""

# 3rd party
import pytest

# models
from api.models.role import Role

# utils
from api.utils.messages.success import SUCCESS
from api.utils.messages.error import VALIDATION

# pylint: disable=too-few-public-methods, no-self-use


@pytest.mark.django_db
class TestRole:
    """Tests role functionality."""

    def test_role_model(self):
        """Tests if role model works as expected."""

        role = Role(**{'role_type': 'user'})
        role.save()
        assert Role.objects.get(role_type='user')
        assert role.__repr__() == f'<Role: {role.role_type}>'
        assert len(Role.objects.all()) >= 1

    def test_create_role_succeeds(self, client):
        """Tests if create role endpoint succeeds.

        Args:
            client (func): DRF's APIClient instance.
        """

        response = client.post('/api/v1/role/', {'role_type': 'user'})
        assert response.status_code == 201
        assert response.data['message'] == SUCCESS['create_entry'].format('user')

    def test_create_role_invalid_values_fails(self, client):
        """Tests if creating role with invalid 'role_type' value fails.

        Args:
            client (func): DRF's APIClient instance.
        """
        response = client.post('/api/v1/role/', {'role_type': 'invalid'})
        assert response.status_code == 400
        assert response.data['message'] == VALIDATION['unsuccessful']
        assert 'role_type' in response.data['errors']

    def test_get_single_department_succeeds(self, client, add_role):
        """Tests if get department endpoint succeeds.

        Args:
            client (func): DRF's APIClient instance.
            add_role (func): Create test role fixture.
        """

        response = client.get(f'/api/v1/role/{add_role.id}/')
        assert response.status_code == 200
        assert response.data['data']['role_type'] == add_role.role_type

    def test_get_single_role_fails(self, client, gen_uuid):
        """Tests getting non-existing role fails.

        Args:
            client (func): DRF's APIClient instance.
            gen_uuid (func): Create uuid fixture.
        """
        response = client.get(f'/api/v1/role/{gen_uuid}/')
        assert response.status_code == 404

    def test_delete_role_succeeds(self, client, add_role):
        """Tests if deleting role succeeds.

        Args:
            client (func): DRF's APIClient instance.
            add_role (func): Create test role fixture.
        """

        response = client.delete(f'/api/v1/role/{add_role.id}/')
        assert response.status_code == 200
        assert response.data['message'] == SUCCESS['delete_entry'].format('role')

    def test_get_department_list_succeeds(self, client, add_role):
        """Tests if getting role list succeeds.

        Args:
            client (func): DRF's APIClient instance.
            add_role (func): Create test role fixture.
        """
        response = client.get('/api/v1/role/')
        assert response.status_code == 200
        assert len(response.data['data']) >= 1

    def test_get_modified_role_list_succeeds(self, client, add_role):
        """Tests if getting role list with specific fields succeeds.

        Args:
            client (func): DRF's APIClient instance.
            add_role (func): Create test role fixture.
        """
        response = client.get('/api/v1/role/?fields=id')
        assert response.status_code == 200
        # Verifies that only 'id' returned for each department in list
        for data in response.data['data']:
            assert len(data) == 1
            assert 'id' in data
