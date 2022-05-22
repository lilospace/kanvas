from email import message
from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
import ipdb
# Create your views here.


class CreateUser(APIView):
    def post(self, request):
        data = request.data
        if data['is_superuser']:
            try:
                super_user = User.objects.create_superuser(
                username=data['username'],
                password=data['password'],
                is_staff=data['is_staff'],
                is_superuser=data['is_superuser']
                )
                return Response({
                    "id": super_user.id,
                    "username": super_user.username,
                    "is_staff": super_user.is_staff,
                    "is_superuser" : super_user.is_superuser
                })
            except:
                if User.objects.get(username=data['username']):
                    return Response({"error": 'User already exist'}, status=status.HTTP_409_CONFLICT)
                return Response('error')
        try:
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
                is_staff=data['is_staff'],
                is_superuser=data['is_superuser']
            )
            return Response({
                "id": user.id,
                "username": user.username,
                "is_staff": user.is_staff,
                "is_superuser" : user.is_superuser
            }, status=status.HTTP_201_CREATED)
        except:
            return Response({"message" : "error for register"}, status=status.HTTP_400_BAD_REQUEST)

        