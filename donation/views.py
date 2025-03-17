from django.shortcuts import render
from .serializer import SerializerDonation
from .models import DonateBlood
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

# Create your views here.


class donationView(APIView):
    # permission_classes=[permissions.IsAuthenticated]
    def post(self,request):
        serializer = SerializerDonation(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Donation Done')
        else:
            return Response(serializer.errors)
        
    def get(self,request):
        queryset = DonateBlood.objects.all()
        serializer = SerializerDonation(queryset,many=True)
        return Response(serializer.data)
    
class searchDonarUsingBloodType(APIView):
    
    def get(self,request,blood_type):
        queryset = DonateBlood.objects.filter(bloodType=blood_type)
        print(queryset)
        serializer = SerializerDonation(queryset,many=True)
        return Response(serializer.data)
        