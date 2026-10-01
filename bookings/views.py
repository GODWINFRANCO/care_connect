from django.shortcuts import render
#rest framework import
from rest_framework.views import APIView
from rest_framework.response import Response
#others import
from bookings.models import Appointment
from bookings.serializers import BookingSerializers
# Create your views here.

class AppointmentsListCreateView(APIView):

    def get(self,request):

        qs = Appointment.objects.all()

        serializer_instance = BookingSerializers(qs,many=True)

        return Response(data=serializer_instance.data)
    
    