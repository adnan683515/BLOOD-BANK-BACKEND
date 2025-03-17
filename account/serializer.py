from rest_framework import serializers
from .models import Registration
from django.contrib.auth.models import User

class allUserlist(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=False)
    usertype = serializers.CharField(required=True)
    mobile  = serializers.CharField(required=True)
    picture = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name', 'mobile','usertype','password','confirm_password','picture']
        
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        mobile = self.validated_data['mobile']
        picture = self.validated_data['picture']
        usertype = self.validated_data['usertype']

        
        if password != confirm_password:
            return  serializers.ValidationError("Password Doesn't Match!")
        
        if User.objects.filter(email=email).exists():
            return serializers.ValidationError('This email Already Exits')
        
        user = User(username=username,first_name=first_name,last_name=last_name,email=email)
        user.set_password(password)
        user.is_active = True
        user.save()
        obj = Registration.objects.create(
            user= user,
            usertype=usertype,
            mobile=mobile,
            picture = picture

        )
        print("final Obj",obj)
        obj.save()
        
        return user
    
    
    
class log_in_serializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    

class userAllDataSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields  = ['id','username','first_name','last_name','email']
    
    
    
class userDetailsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')  # Access email via user 
    first_name = serializers.CharField(source='user.first_name')  # Access first 
    last_name = serializers.CharField(source='user.last_name')  # Access last name 

    class Meta:
        model = Registration
        fields = ['id','username','email', 'first_name', 'last_name', 'mobile','usertype','mobile','picture']