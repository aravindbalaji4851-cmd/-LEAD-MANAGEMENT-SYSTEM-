from django.shortcuts import render

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from rest_framework_simplejwt.authentication import JWTAuthentication

from leads.models import Lead
from leads.serializers import LeadSerializer
from leads.permissions import IsCreator

class LeadCreateListView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        instances = Lead.objects.filter(created_by=request.user)

        serializer = LeadSerializer(instances,many=True)

        return Response(data=serializer.data)

    def post(self,request):

        form_data = request.data

        serializer = LeadSerializer(data=form_data)

        if serializer.is_valid():

            serializer.save(created_by=request.user)

            return Response(data=serializer.data)

        else: return Response(data=serializer.errors)

class LeadRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    serializer_class = LeadSerializer

    queryset = Lead.objects.all()

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated,IsCreator]