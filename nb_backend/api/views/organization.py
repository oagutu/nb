"""
api/views/organization.py
Organization views module.
"""

# django
from django.utils import timezone

# rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# serializers
from ..serializers.organization import OrganizationSerializer

# models
from ..models.organization import Organization

# helpers
from ..utils.helpers.model import get_single_entry, delete_check

# messages
from ..utils.messages import create_message

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
            return Response(
                create_message(data['name'], data=data, msg_key='create_entry'),
                status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """Get list of organizations

        Args:
            request (object): rest_framework request object.

        Returns:
            object: rest_framework Response instance.
        """

        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        data = serializer.data
        return Response(
            create_message('organization', data=data, msg_key='fetch_entries'),
            status=status.HTTP_200_OK)

# pylint: disable=invalid-name, unused-argument
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
            return Response(
                create_message('organization', data=serializer.data, msg_key='fetch_entries'),
                status=status.HTTP_200_OK)

        except Organization.DoesNotExist:
            return Response(
                create_message('organization', msg_key='fetch_entry', success=False),
                status=status.HTTP_404_NOT_FOUND)


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
                data = serializer.data
                return Response(
                    create_message('organization', data=serializer.data, msg_key='update_entry'),
                    status=status.HTTP_200_OK)
            else:
                data = {'errors': serializer.errors, 'status': 'error'}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

        except Organization.DoesNotExist as e:
            return Response(
                {'status': 'error', 'message':  e.__str__()}, status=status.HTTP_404_NOT_FOUND)

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
                return Response(
                    create_message(organization.name, msg_key='delete_entry'),
                    status=status.HTTP_200_OK)

        except Organization.DoesNotExist as e:
            return Response(
                {'status': 'error', 'message':  e.__str__()}, status=status.HTTP_404_NOT_FOUND)
