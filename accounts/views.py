from django.shortcuts import render

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.serializers import UserSerializer
from accounts.models import User

class SignUpView(APIView):

    def post(self,request):

        form_data = request.data

        serializer = UserSerializer(data=form_data)

        if serializer.is_valid():

            cleaned_data = serializer.validated_data

            instance = User.objects.create_user(** cleaned_data)

            serializer_inst = UserSerializer(instance)

            return Response(data=serializer_inst.data)

        else: return Response(data=serializer.errors)
            

class ProfileRetreiveView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        instance = request.user

        serializer = UserSerializer(instance)

        return Response(data=serializer.data)