from .models import DonateBlood
from rest_framework import serializers
from account.serializer import userAllDataSerializer

class SerializerDonation(serializers.ModelSerializer):
    
    class Meta:
        model = DonateBlood
        fields ='__all__'