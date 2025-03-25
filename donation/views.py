from django.shortcuts import render
from .serializer import SerializerDonation,SerializerBloodRequest,SerializerBloodRequestForGET
from .models import DonateBlood,BloodRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

# Create your views here.


class donationView(APIView):
    # permission_classes=[permissions.IsAuthenticated]
    def post(self,request):

        serializer = SerializerDonation(data=request.data)

        if serializer.is_valid():
            obj = serializer.save()
            obj.user = request.user
            obj.done=True
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
            
            
        try:
            # Try to get the object
            obj = DonateBlood.objects.get(user=pk)
            
            serializer = SerializerDonation(obj, many=False)
            return Response(serializer.data)
        except DonateBlood.DoesNotExist:
            # Handle the case where the object does not exist
            print("Something went wrong: Object not found")
            return Response("Donate record not found, please add this")


        
            
        
        
        
class requestBloddApiView(APIView):
    def post(self,request):
        serializer = SerializerBloodRequest(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Blood Request Done")
        
        return Response(serializer.errors)

    def get(self,request):
        queryset = BloodRequest.objects.all()
        serializer = SerializerBloodRequestForGET(queryset,many=True)
        return Response(serializer.data)
        
        
class bloodRequestShowingByuserId(APIView):
    
    def get(self,request,pk):
        queryset = BloodRequest.objects.filter(DonateBlood=pk)
        serializer = SerializerBloodRequestForGET(queryset,many=True)
        return Response(serializer.data)
