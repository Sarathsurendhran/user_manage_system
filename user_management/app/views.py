from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from. models import Users
from django.shortcuts import get_object_or_404  


class ProtectedView(APIView):
    def get(self, request, id):
        user = get_object_or_404(Users, id=id)
        if user.is_premium:
            return Response("access granted", status=status.HTTP_200_OK)
        return Response("you do not have permission", status=status.HTTP_401_UNAUTHORIZED)


class RoleView(APIView):
    def get(self, request, id):
        user = get_object_or_404(Users, id=id)
        if user:
            return Response("access granted", status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
        
        