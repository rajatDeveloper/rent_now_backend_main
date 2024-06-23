from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse 
from django.shortcuts import get_object_or_404
from rest_framework import status 
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend  
from rent_now.models import Address, Category , RentRequest , RentPost , RentOrder  , User
from .serializers import AddressSerializer , CategorySerializer , RentRequestSerializer , RentPostSerializer , RentPostCreateSerializer
from rest_framework.response import Response
from rest_framework.permissions import  IsAuthenticated


#Address End points 
# get address model of user abd create address model 
class AddressListUpdateView(generics.ListCreateAPIView):
    
    # permission_classes = [IsAuthenticated]
    
    serializer_class = AddressSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        return Address.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        request.data['user'] = user.id
        serializer = AddressSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
# Category View  
# two end points one to get all category and create a category   
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# RentRequest 
# two end points one to get all rent request and create a rent request
class RentRequestListCreateView(generics.ListCreateAPIView):
    queryset = RentRequest.objects.all()
    serializer_class = RentRequestSerializer   
    
    
# get rent post model of user 
class RentPostListView(generics.ListAPIView):
    
    # permission_classes = [IsAuthenticated]
    
    serializer_class = RentPostSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        return RentPost.objects.filter(user=user)
    
# get rent post model of user 
class RentPostCreateView(generics.CreateAPIView):
    
    # permission_classes = [IsAuthenticated]
    
    serializer_class = RentPostCreateSerializer


    def create(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        request.data['user'] = user.id
        serializer = RentPostCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class RentPostGetSingleView(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = RentPost.objects.all()
    serializer_class = RentPostSerializer
    
 
      
    
    








