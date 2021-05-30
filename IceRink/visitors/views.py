from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from json import loads
from .utils import VisitorApi
from .serializer import VisitorRegisterSerializer
from .serializer import VisitorLoginSerializer

class VisitorAuthAPI(APIView):
    def __init__(self):
        super().__init__()
        self.api = VisitorApi()
    def get(self, request: HttpRequest):
        try:
            self.api.logout_visitor(request)
            return Response(status=200)
        except:
            return Response(status=400)

    def post(self, request: HttpRequest):
        login_data = loads(request.body)
        login_data_serializer = VisitorLoginSerializer(data=login_data)
        if not login_data_serializer.is_valid():
            try:
                self.api.login_visitor(request, login_data_serializer.data)
                return Response(status=200)
            except:
                return Response(status=400)
        return Response(status=400)

    def put(self, request: HttpRequest):
        register_data = loads(request.body)
        register_data_serializer = VisitorRegisterSerializer(data=register_data)
        if not register_data_serializer.is_valid():
            try:
                self.api.register_visitor(register_data_serializer.data)
                return Response(status=200)
            except:
                return Response(status=400)
        return Response(status=400)