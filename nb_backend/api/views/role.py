"""
api/views/role.py
role views module.
"""

# rest_framework
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

# models
from api.models.role import Role
# serializer
from api.serializers.role import RoleSerializer
# utils: messages
from api.utils.messages import create_response
# utils: helpers
from api.utils.helpers.model import entry_exists, delete_check
from api.utils.helpers.query_params import get_query_fields

# pylint: disable=no-self-use, invalid-name, unused-argument


class RoleViewSet(ViewSet):
    """Department viewset class."""

    queryset = Role.objects.all()
    fields = ('id', 'created_on', 'role_type')
    serializer = RoleSerializer

    def create(self, request):
        """Creates new role record.

        Args:
            self (obj): RoleViewSet instance.
            request (obj): rest_framework request object.
        Returns:
            obj : rest_framework Response instance.
        """

        data = request.data
        serializer = self.serializer(data=data)
        resp_data = {'msg_key': 'unsuccessful', 'success': False}
        if serializer.is_valid():
            resp_data = {'msg_key': 'create_entry', 'status': 'created'}
            serializer.save()
            data = {'data': serializer.data}
            args = (request.data['role_type'], )
        else:
            args = ()
            data = {'errors': serializer.errors}

        return Response(*create_response(*args, payload=data, **resp_data))

    def retrieve(self, request, pk):
        """Retrieves single role instance.

        Args:
            self (obj): RoleViewSet instance.
            request (obj): rest_framework request object.
            pk (int): Primary key of object to be retrieved

        Returns:
            obj : rest_framework Response instance.
        """

        fields = get_query_fields(request) or self.fields
        role = entry_exists(Role, pk)
        serializer = self.serializer(role, fields=fields)
        return Response(*create_response(
            'role', payload={'data': serializer.data}, msg_key='fetch_entries', status='ok'
        ))

    def destroy(self, request, pk):
        """Deletes a role instance.

        Args:
            self (obj): RoleViewSet instance.
            request (obj): rest_framework request object.
            pk (int): Primary key of object to be deleted.

        Returns:
            obj : rest_framework Response instance.
        """

        role = entry_exists(Role, pk)
        role.delete()
        return Response(*create_response('role', msg_key='delete_entry', status='ok'))

    def list(self, request):
        """Gets all roles.

        Args:
            self (obj): RoleViewSet instance.
            request (obj): rest_framework request object.

        Returns:
            obj : rest_framework Response instance.
        """

        fields = get_query_fields(request) or self.fields
        filter_params = {} if request.query_params.get('deleted', False) else {'deleted': False}
        roles = self.queryset.filter(**filter_params)
        serializer = self.serializer(roles, fields=fields, many=True)
        payload = {'count': len(serializer.data), 'data': serializer.data}
        return Response(*create_response(
            'role', payload=payload, msg_key='fetch_entries', status='ok'
        ))
