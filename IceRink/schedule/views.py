from django.http import HttpRequest
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from json import loads
from json import dumps
from database.utils import DataBaseAPI
from database.utils import ReminderAPI
from .serializer import VisitorRecordSerializer
from .serializer import UserNameSerializer


class SheduleView(APIView):
    def __init__(self):
        super().__init__()
        self.db_api = DataBaseAPI()
        self.serializer = VisitorRecordSerializer

    def post(self, request: HttpRequest):
        data = loads(request.body)
        data_serializer = self.serializer(data=data)
        if not data_serializer.is_valid():
            return Response(status=400)
        try:
            self.db_api.make_record(data_serializer.data)
            return Response(status=200)
        except:
            return Response(status=400)


class Reminder(APIView):
    def __init__(self):
        super().__init__()
        self.record_serializer = VisitorRecordSerializer
        self.username_serializer = UserNameSerializer
        self.reminder_tool = ReminderAPI()

    def post(self, request: HttpRequest):
        data = loads(request.body)
        username = self.username_serializer(data=data)
        if not username.is_valid():
            return Response(status=400)
        try:
            remind_record = self.reminder_tool.get_reminder(username.data)
            record = self.record_serializer(data=remind_record)
            return Response(dumps(record), status=200)
        except:
            return Response(status=400)

