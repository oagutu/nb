"""Organization tests module."""

# 3rd party
import pytest

# models
from ..models.organization import Organization

# utils
from ..utils.messages.success import SUCCESS
from ..utils.messages.error import VALIDATION

@pytest.mark.django_db
class TestOrganization:
    """Tests Organization model"""

    # pylint: disable=unused-argument

    def test_organization_model(self, org_data):
        """Tests if an organization model works as expected.

        Args:
            org_data (dict): Organization test data fixture.
        """

        organization = Organization(**org_data['testorg'])
        organization.save()
        assert Organization.objects.get(name='TestOrg')
        assert len(Organization.objects.all()) >= 1


    def test_create_organization_record_succeeds(self, client, org_data):
        """Tests if create organization endpoint succeeds.

        Args:
            client (obj): DRF's APIClient instance.
            org_data (dict): Organization test data fixture.
        """

        response = client.post('/api/v1/organization/', org_data['testorg'])
        assert response.status_code == 201
        assert response.data['message'] == SUCCESS['create_entry'].format(
            org_data['testorg']['name'])

    def test_create_organization_record_fails(self, client, org_data, add_org):
        """Tests creting alreday existing org fails.

        Args:
            client (obj): DRF's APIClient instance.
            org_data (dict): Organization test data fixture.
            add_org (func): Fixture that creates new orgnization db record
        """

        response = client.post('/api/v1/organization/', org_data['testorgtwo'])
        assert response.status_code == 400
        assert response.data['message'] == VALIDATION['unsuccessful']

    def test_get_organization_succeeds(self, client, add_org):
        """Tests getting existing org succeeds.

        Args:
            client (obj): DRF's APIClient instance.
            add_org (func): Fixture that creates new orgnization db record
        """

        response = client.get(f'/api/v1/organization/{add_org.id}/')

        assert response.status_code == 200
        assert response.data['data']['name'] == add_org.name

    def test_get_organization_fails(self, client, gen_uuid):
        """Tests getting existing org fails.

        Args:
            client (obj): DRF's APIClient instance.
            gen_uuid (str): UUID instance fixture.
        """

        response = client.get(f'/api/v1/organization/{gen_uuid}/')

        assert response.status_code == 404
        assert response.data['message'] == VALIDATION['fetch_entry'].format('organization')


    def test_get_organization_list_succeeds(self, client, add_org):
        """Tests getting list of orgs succeeds

        Args:
            client (obj): DRF's APIClient instance.
            add_org (func): Fixture that creates new orgnization db record
        """

        response = client.get('/api/v1/organization/')

        assert response.status_code == 200
        assert response.data['message'] == SUCCESS['fetch_entries'].format('organization')
        assert len(response.data['data']) >= 1

    def test_update_org_succeeds(self, client, add_org):
        """Tests updating organization info succeeds

        Args:
            client (obj): DRF's APIClient instance.
            add_org (func): Fixture that creates new orgnization db record.
        """

        updated_data = {'domain': 'updated_domain'}
        response = client.patch(f'/api/v1/organization/{add_org.id}/', updated_data)

        assert response.status_code == 200
        assert response.data['message'] == SUCCESS['update_entry'].format('organization')
        assert response.data['data']['domain'] == updated_data['domain']

    def test_update_non_existent_org_fails(self, client, gen_uuid):
        """Tests updating non-existing organization fails

        Args:
            client (obj): DRF's APIClient instance.
            gen_uuid (str): UUID instance fixture.
        """

        updated_data = {'domain': 'updated_domain'}
        response = client.patch(f'/api/v1/organization/{gen_uuid}/', updated_data)

        assert response.status_code == 404
        assert response.data['message'] == VALIDATION['fetch_entry'].format('organization')

    def test_update_org_fails(self, client, add_org):
        """Tests updating organization using invalid info fails

        Args:
            client (obj): DRF's APIClient instance.
            add_org (func): Fixture that creates new orgnization db record.
        """
        updated_data = {'domain': ''}
        response = client.patch(f'/api/v1/organization/{add_org.id}/', updated_data)

        assert response.status_code == 400
        assert response.data['message'] == VALIDATION['unsuccessful']
        assert response.data['errors']['domain'][0] == 'This field may not be blank.'


    def test_delete_org_succeeds(self, client, add_org):
        """Tests deleting organization succeeds.

        Args:
            client (obj): DRF's APIClient instance.
            add_org (func): Fixture that creates new orgnization db record.
        """

        response = client.delete(f'/api/v1/organization/{add_org.id}/')

        assert response.status_code == 200
        assert response.data['message'] == SUCCESS['delete_entry'].format(add_org.name)

    def test_delete_org_failss(self, client, gen_uuid):
        """Tests deleting non-existent irg fails

        Args:
            client (obj): DRF's APIClient instance.
            gen_uuid (str): UUID instance fixture.
        """

        response = client.delete(f'/api/v1/organization/{gen_uuid}/')

        assert response.status_code == 404
        assert response.data['message'] == VALIDATION['fetch_entry'].format('organization')
