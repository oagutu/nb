"""
api/views/organization.py
Organization views module.
"""

# django
from django.utils import timezone

# rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response

# serializers
from ..serializers.organization import OrganizationSerializer

# models
from ..models.organization import Organization

# helpers
from ..utils.helpers.model import get_single_entry, delete_check

# messages
from ..utils.messages import create_response

# pylint: disable=unused-argument
class OrganizationView(APIView):
    """Main organization api view class."""

    def post(self, request):
        """Create new organization record/entry.

        Args:
            request (object): rest_framework request object.

        Returns:
            object: rest_framework Response instance.
        """

        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(*create_response(
                data['name'], payload={'data':data}, msg_key='create_entry', status='created'))

        return Response(*create_response(
            payload={'errors': serializer.errors}, msg_key='unsuccessful', success=False))

    def get(self, request):
        """Get list of organizations

        Args:
            request (object): rest_framework request object.

        Returns:
            object: rest_framework Response instance.
        """

        organizations = Organization.objects.filter(deleted=False)
        serializer = OrganizationSerializer(organizations, many=True)
        data = serializer.data
        print('data: ', data)
        return Response(*create_response(
            'organization', payload={'data':data}, msg_key='fetch_entries', status='ok'))

# pylint: disable=invalid-name
class OrganizationSingleView(APIView):
    """Single organization api view class."""

    def get(self, request, pk):
        """Fetch single organization entry

        Args:
            request (object): rest_framework request object.
            pk (str): Key of organization to be fetched

        Returns:
            object: rest_framework Response instance.
        """
        try:
            organization = get_single_entry(Organization, pk)
            serializer = OrganizationSerializer(organization)
            return Response(*create_response(
                'organization',
                payload={'data':serializer.data},
                msg_key='fetch_entries',
                status='ok'))

        except Organization.DoesNotExist:
            return Response(*create_response(
                'organization', msg_key='fetch_entry', success=False, status='not_found'))

    def patch(self, request, pk):
        """Updates/Edits organization entry.

        Args:
            request (object): rest_framework request object.
            pk (str): Key of organization to be fetched

        Returns:
            object: rest_framework Response instance.
        """

        try:
            organization = get_single_entry(Organization, pk)
            request.data.update({'edited_on': timezone.now()})
            serializer = OrganizationSerializer(organization, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = {'data': serializer.data}
                return Response(*create_response(
                    'organization', payload=data, msg_key='update_entry', status='ok'))

            data = {'errors': serializer.errors}
            return Response(*create_response(
                payload=data, status='bad_request', msg_key='unsuccessful', success=False))

        except Organization.DoesNotExist:
            return Response(*create_response(
                'organization', status='not_found', success=False, msg_key='fetch_entry'))

    def delete(self, request, pk):
        """Soft deletes sorganization entry

        Args:
            request (object): rest_framework request object.
            pk (str): Key of organization to be fetched

        Returns:
            object: rest_framework Response instance.
        """

        try:
            organization = get_single_entry(Organization, pk)
            delete_check(request, organization)
            data = {'deleted': True, 'deleted_on': timezone.now()}
            serializer = OrganizationSerializer(organization, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(*create_response(
                    organization.name, msg_key='delete_entry', status='ok'))

        except Organization.DoesNotExist:
            return Response(*create_response(
                'organization', status='not_found', success=False, msg_key='fetch_entry'))
