from .models import DonateBlood,BloodRequest
from rest_framework import serializers
from account.serializer import userAllDataSerializer

class SerializerDonation(serializers.ModelSerializer):
    
    class Meta:
        model = DonateBlood
        fields ='__all__'
        
     
class SerializerBloodRequest(serializers.ModelSerializer):

    
    class Meta:
        model = BloodRequest
        fields = '__all__'
     
        
class SerializerBloodRequestForGET(serializers.ModelSerializer):
    user = userAllDataSerializer(read_only=True)
    DonateBlood = SerializerDonation(read_only=True)
    class Meta:
        model = BloodRequest
        fields = '__all__'