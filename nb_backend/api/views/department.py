"""
api/views/department.py
Department views module.
"""

# django
from django.utils import timezone
# rest_framework
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

# models
from api.models.department import Department
# serializer
from api.serializers.department import DepartmentSerializer
# utils: messages
from api.utils.messages import create_response
# utils: helpers
from api.utils.helpers.model import entry_exists, delete_check
from api.utils.helpers.query_params import get_query_fields

# pylint: disable=no-self-use, invalid-name, unused-argument

class DepartmentViewSet(ViewSet):
    """Department viewset class."""

    queryset = Department.objects.all()
    fields = ('id', 'name', 'description', 'members', 'organization')

    def create(self, request):
        """Creates new department record.

        Args:
            self (obj): DepartmentViewSet instance.
            request (obj): rest_framework request object.
        Returns:
            obj : rest_framework Response instance.
        """

        data = request.data
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(*create_response(
                data['name'], payload={'data':data}, msg_key='create_entry', status='created'))

        return Response(*create_response(
            payload={'errors': serializer.errors}, msg_key='unsuccessful', success=False))

    def retrieve(self, request, pk):
        """Retrieves single department instance.

        Args:
            self (obj): DepartmentViewSet instance.
            request (obj): rest_framework request object.
            pk (int): Primary key of object to be retrieved

        Returns:
            obj : rest_framework Response instance.
        """

        fields = get_query_fields(request) or self.fields
        department = entry_exists(Department, pk)
        serializer = DepartmentSerializer(department, fields=fields)
        return Response(*create_response(
            'department', payload={'data': serializer.data}, msg_key='fetch_entries', status='ok'
        ))

    def partial_update(self, request, pk):
        """Partially updates an existing department record.

        Args:
            self (obj): DepartmentViewSet instance.
            request (obj): rest_framework request object.
            pk (int): Primary key of object to be updated.

        Returns:
            obj : rest_framework Response instance.
        """

        department = entry_exists(Department, pk)
        request.data.update({'edited_on': timezone.now()})
        serializer = DepartmentSerializer(department, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {'data': serializer.data}
            return Response(*create_response(
                'organization', payload=data, msg_key='update_entry', status='ok'))

        data = {'errors': serializer.errors}
        return Response(*create_response(
            payload=data, status='bad_request', msg_key='unsuccessful', success=False))


    def destroy(self, request, pk):
        """Deletes a department instance.

        Args:
            self (obj): DepartmentViewSet instance.
            request (obj): rest_framework request object.
            pk (int): Primary key of object to be deleted.

        Returns:
            obj : rest_framework Response instance.
        """

        department = entry_exists(Department, pk)
        delete_check(request, department)
        delete_details = {'deleted_on': timezone.now(), 'deleted': True}
        serializer = DepartmentSerializer(
            department, data=delete_details, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {'data': serializer.data}
            return Response(*create_response(
                'department', payload=data, msg_key='delete_entry', status='ok'))
        data = {'data': serializer.errors}
        return Response(*create_response(
            'department', msg_key='already_deleted', success=False))


    def list(self, request):
        """Gets all departments.

        Args:
            self (obj): DepartmentViewSet instance.
            request (obj): rest_framework request object.

        Returns:
            obj : rest_framework Response instance.
        """

        fields = get_query_fields(request) or self.fields
        filter_params = {} if request.query_params.get('deleted', False) else {'deleted': False}
        departments = self.queryset.filter(**filter_params)
        serializer = DepartmentSerializer(departments, fields=fields, many=True)
        payload = {'count': len(serializer.data), 'data': serializer.data}
        return Response(*create_response(
            'department', payload=payload, msg_key='fetch_entries', status='ok'
        ))
