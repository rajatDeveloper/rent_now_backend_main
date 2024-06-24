from rest_framework import serializers
from rent_now.models import Address , User  , Category , RentRequest , RentPost , User  , RentOrder

#will have all serlizers for the api here 


# Address 
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        
# Category 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
# Rent Type  
       
class RentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentRequest
        fields = '__all__'                  
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email']                  
        
            
class RentPostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    address = AddressSerializer()
    rent_request = RentRequestSerializer(many=True)    
    class Meta:
        model = RentPost
        fields = '__all__'        

class RentPostCreateSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = RentPost
        fields = '__all__'            
        

class RentOrderCreateSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = RentOrder
        fields = '__all__'    
        

class RentOrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    rent_post = RentPostSerializer()
    rent_request = RentRequestSerializer()
    user_address = AddressSerializer()
    
    class Meta:
        model = RentOrder
        fields = '__all__'                                     
        