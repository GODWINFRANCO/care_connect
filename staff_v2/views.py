from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from staff.models import Doctor
from staff_v2.serializers import DoctorSerializer,UserSerializer
# Create your views here.
class DoctorListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self,request):
    
            qs = Doctor.objects.all() #qs=> pynt => serializer
    
            serializers_instance = DoctorSerializer(qs,many=True) 
    
            return Response(data=serializers_instance.data)
    
    def post(self,request):

          form_data = request.data

          serializer_instance = DoctorSerializer(data=form_data)

          if serializer_instance.is_valid():
            
            cleaned_data = serializer_instance.validated_data
               
            Doctor.objects.create(**cleaned_data)
            
            return Response(data=serializer_instance.validated_data)
          
          else:
              
              return Response(data=serializer_instance.errors)

class DoctorRetrieveUpdateDeleteView(APIView):

     def put(self,request,pk=None):

          form_data = request.data

          serializer_instance = DoctorSerializer(data=form_data)

          if serializer_instance.is_valid():

               cleaned_data = serializer_instance.validated_data

               Doctor.objects.filter(id=pk).update(**cleaned_data)

               return Response(data=serializer_instance.validated_data)

          else:

               return Response(data=serializer_instance.errors)

class AdminCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            # User.objects.create(**cleaned_data) X password encrypt

            # User.objects.create_user(**cleaned_data) X not an admin user

            User.objects.create_superuser(**cleaned_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)
