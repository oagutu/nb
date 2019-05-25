"""Department tests module."""

# 3rd party
import pytest

# models
from api.models.department import Department

# utils
from api.utils.messages.success import SUCCESS
from api.utils.messages.error import VALIDATION

# pylint: disable=too-few-public-methods, no-self-use


@pytest.mark.django_db
class TestDepartment:
    """Tests department functionality."""

    def test_department_model(self, add_org, dept_data):
        """Tests if department model works as expected.

        Args:
            add_org (func): Create test Organization fixture.
            dept_data (func): Organization test data fixture.
        """

        data = dept_data['test_dept']
        data.update({'organization': add_org})
        department = Department(**data)
        department.save()
        assert Department.objects.get(name=data['name'])
        assert len(Department.objects.all()) >= 1

    def test_create_department_succeeds(self, client, dept_data):
        """Tests if create department endpoint succeeds.

        Args:
            client (func: DRF's APIClient instance.
            dept_data (func): Departement test data fixture.
        """

        data = dept_data['test_dept']
        response = client.post('/api/v1/department/', data)
        assert response.status_code == 201
        assert response.data['message'] == SUCCESS['create_entry'].format(
            data['name'])

    def test_create_department_invalid_values_fails(self, client, dept_data):
        """Tests if creating department with invalid 'name' value fails.

        Args:
            client (func): DRF's APIClient instance.
            dept_data (func): Departement test data fixture.
        """
        data = dept_data['test_dept']
        data.update({'name': "$$$"})
        response = client.post('/api/v1/department/', data)
        assert response.status_code == 400
        assert response.data['message'] == VALIDATION['unsuccessful']
        assert 'name' in response.data['errors']

    def test_get_single_department_succeeds(self, client, add_dept):
        """Tests if get department endpoint succeeds.

        Args:
            client (func): DRF's APIClient instance.
            add_dept (func): Create test Department fixture.
        """

        response = client.get(f'/api/v1/department/{add_dept.id}/')
        assert response.status_code == 200
        assert response.data['data']['name'] == add_dept.name

    def test_get_single_department_fails(self, client, gen_uuid):
        """Tests getting non-existing department fails.

        Args:
            client (func): DRF's APIClient instance.
            gen_uuid (func): Create uuid fixture.
        """
        response = client.get(f'/api/v1/department/{gen_uuid}/')
        assert response.status_code == 404

    def test_update_department_succeeds(self, client, add_dept):
        """Tests if update department endpoint succeeds.

        Args:
            client (func): DRF's APIClient instance.
            add_dept (func): Create test Department fixture.
        """

        data = {"name": "updated_department"}
        response = client.patch(f'/api/v1/department/{add_dept.id}/', data)
        assert response.status_code == 200
        assert response.data['data']['name'] == data['name']

    def test_update_department_fails(self, client, add_dept, gen_uuid):
        """Tests if update department with invalid data fails.

        Args:
            client (func): DRF's APIClient instance.
            add_dept (func): Create test Department fixture.
            gen_uuid (func): Create uuid fixture.
        """

        data = {"organization": gen_uuid}
        response = client.patch(f'/api/v1/department/{add_dept.id}/', data)
        assert response.status_code == 400
        assert 'organization' in response.data['errors']

    def test_delete_department_succeeds(self, client, add_dept):
        """Tests if deleting department succeeds.

        Args:
            client (func): DRF's APIClient instance.
            add_dept (func): Create test Department fixture.
        """

        response = client.delete(f'/api/v1/department/{add_dept.id}/')
        assert response.status_code == 200
        assert response.data['message'] == SUCCESS['delete_entry'].format('department')

    def test_delete_already_deleted_department_fails(self, client, add_dept):
        """Tests if deleting already deleted department failss.

        Args:
            client (func): DRF's APIClient instance.
            add_dept (func): Create test Department fixture.
        """
        add_dept.deleted = True
        add_dept.save()
        response = client.delete(f'/api/v1/department/{add_dept.id}/')
        assert response.status_code == 400
        assert response.data['message'] == VALIDATION['already_deleted'].format(add_dept.name)

    def test_get_department_list_succeeds(self, client, add_dept):
        """Tests if getting department list succeeds.

        Args:
            client (func): DRF's APIClient instance.
            add_dept (func): Create test Department fixture.
        """
        response = client.get('/api/v1/department/')
        assert response.status_code == 200
        assert len(response.data['data']) >= 1

    def test_get_modified_department_list_succeeds(self, client, add_dept):
        """Tests if getting department list with specific fields succeeds.

        Args:
            client (func): DRF's APIClient instance.
            add_dept (func): Create test Department fixture.
        """
        response = client.get('/api/v1/department/?fields=id')
        assert response.status_code == 200
        # Verifies that only 'id' returned for each department in list
        for data in response.data['data']:
            assert len(data) == 1
            assert 'id' in data
