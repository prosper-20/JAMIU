from django.shortcuts import render, get_object_or_404
from .serializers import PropertySerializer, AgentSerializer , ListingSerializer ,InquirySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from listings.models import  Property,Agent, Listing , Inquiry
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class Propertyhomepage(APIView):
    def get(self, request):
        property = Property.objects.all()
        serializer = PropertySerializer(property, many=True)
        filter_backends = [DjangoFilterBackend , SearchFilter]
        filterset_fields = ["Property"]
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def post(self, request):
        new_property = Property.objects.all()
        serializer = PropertySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class Propertydetailpage(APIView):
    def get (self, request,pk):
        property = get_object_or_404(Property, id=pk)
        serializer = PropertySerializer(property)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request,pk):
        property = get_object_or_404(Property, id=pk)
        serializer = PropertySerializer(property, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self,request,pk):
        property = get_object_or_404(Property, id=pk)
        property.delete()
        return Response( status=status.HTTP_204_NO_CONTENT)
    


class Agents(APIView):
    def get(self, request):
        agent = Agent.objects.all()
        serializer = AgentSerializer(agent, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = Agent.objects.all()
        serializer = AgentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class Listings(APIView):
    def get(self, request):
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings,many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = Listing.objects.all()
        serializer = ListingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class Inquirylist(APIView):
    def get(self, request):
        inquiry= Inquiry.objects.all()
        serializer = InquirySerializer(inquiry, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = Inquiry.objects.all()
        serializer = InquirySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
# Create your views here.
