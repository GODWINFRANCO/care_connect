from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from staff.models import Doctor
from staff_v2.serializers import DoctorSerializer
# Create your views here.
class DoctorListCreateView(APIView):

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