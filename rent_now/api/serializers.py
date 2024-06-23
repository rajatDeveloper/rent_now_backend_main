from rest_framework import serializers
from rent_now.models import Address , User  

#will have all serlizers for the api here 

# Address 
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'