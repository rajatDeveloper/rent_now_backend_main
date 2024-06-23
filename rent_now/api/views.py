from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse 
from django.shortcuts import get_object_or_404
from rest_framework import status 
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend  
from rent_now.models import Address, Category , RentRequest , RentPost , RentOrder  , User
from .serializers import AddressSerializer
from rest_framework.response import Response

#Address End points 

class AddressListUpdateView(generics.ListCreateAPIView):
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
    








