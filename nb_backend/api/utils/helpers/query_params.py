"""Request query parameter processing module"""


def get_query_fields(request):
    """Gets fields specified under query parameters.

        This helps limit the data returned in the response thereby saving on resources
        eg processing time and memory.

        Args:
            request (object): DRF Request object.

        Returns:
            tuple: If fields specified in request params else returns None.
    """

    fields = request.query_params.get('fields', None)
    if fields:
        fields = fields.split(',')
        fields = tuple(map(lambda name: name.lower(), fields))
    return fields
