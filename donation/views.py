from django.shortcuts import render
from .serializer import SerializerDonation,SerializerBloodRequest
from .models import DonateBlood,BloodRequest
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
        
class donateCardDetails(APIView):

    def get(self,request,pk):
        obj = DonateBlood.objects.get(user=pk)
        if(obj):
            serializer = SerializerDonation(obj,many=False)
            return Response(serializer.data)
        return Response("donate not found please add this")
        
        
class requestBloddApiView(APIView):
    
    
    def post(self,request):
        serializer = SerializerBloodRequest(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Blood Request Done")
        
        return Response(serializer.errors)
    
    
    def get(self,request):
        queryset = BloodRequest.objects.all()
        serializer = SerializerBloodRequest(queryset,many=True)
        return Response(serializer.data)
        