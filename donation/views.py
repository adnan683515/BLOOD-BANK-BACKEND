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
        print("data")
        print(request.user)
        serializer = SerializerDonation(data=request.data)
        print(request.data.get('user_id'))
        if serializer.is_valid():
            obj = serializer.save()
            obj.user = request.user
            obj.save()
            
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
        