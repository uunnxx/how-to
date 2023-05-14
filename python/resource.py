class Resource:
    __resourceData = []

    def __init__(self, request, data_source):
        self.request = request
        self.data_source = data_source

    def get(self, request):
        return Response(200, get_representation(request.url, resource_data))

    def put(self, request):
        return Response(405)

    def post(self, request):
        return Response(405)

    def delete(self, request):
        return Response(405)
