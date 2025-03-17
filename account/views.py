from django.shortcuts import render,redirect
from rest_framework.response import Response
from .models import Registration
from rest_framework.views import APIView
from .serializer import RegistrationSerializer,log_in_serializer,userDetailsSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import permissions
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class RegisterApiView(APIView):
    

    def post(self,request):
        username = request.data.get('username')
        
        email = request.data.get('email')
        if(request.data['password'] != request.data['confirm_password']):
            return Response({"error": "Password Doesn't match "}, status=400)
        if User.objects.filter(username=username):
            return Response({"error": "Username already exists register"}, status=400)
    
        if User.objects.filter(email=email):
            return Response({"error": "Email already exists"}, status=400)
        
        serializer = RegistrationSerializer(data=request.data)
        
        print("serializer",serializer)
        print("request data",request.data)
        if serializer.is_valid():
            obj = serializer.save()
            print("serilaizer obj",obj)
            token = default_token_generator.make_token(obj)
            uid = urlsafe_base64_encode(force_bytes(obj.pk))
            obj.save()
            return Response("ok")
        
        else:
            return Response(serializer.errors)
        
    def get(self,request,format=None):
        queryset  = Registration.objects.all()
        serializer = userDetailsSerializer(queryset,many=True)
        return Response(serializer.data)
    

    

class DetailsUserView(APIView):
    def get(self,request,pk):
        queryset = Registration.objects.get(pk=pk)
        serializer = userDetailsSerializer(queryset, many=False)
        return Response(serializer.data)
    

        



class LoginApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request,format=None):
        serializer = log_in_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
        
            user = authenticate(username=username, password=password)
            details =Registration.objects.get(user=user)
            print(details.picture)
            if user:
            
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)  
                
                return Response({
                    'message': "Login successful",
                    'token': token.key,
                    'user':user.pk,
                    'is_stuff':user.is_staff,
                    'pic':details.picture
                })
                
            else:
                return Response({'error': "Invalid Credential"})

        return Response(serializer.errors)


class userDetalisView(APIView):
    def get(self,request,foramt=None):
        obj = Registration.objects.all()
        serialzer = userDetailsSerializer(obj,many=True)
        return  Response(serialzer.data)
    
    

class logoutView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        logout(request)
        return redirect('login')