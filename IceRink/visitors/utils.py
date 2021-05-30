from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.models import User


class VisitorApi:
    def logout_visitor(self, request):
        logout(request)

    def login_visitor(self, request, visitor_data):
        visitor = authenticate(username=visitor_data['username'], password=visitor_data['password'])
        if visitor:
            login(request, visitor)
        raise Exception

    def register_visitor(self, visitor_data):
        User(**visitor_data).save()
