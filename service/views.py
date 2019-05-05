from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from service.serializers import BrandSerializer, ContactNumberSerializer, \
    AddressSerializer, CategorySerializer, HoursOfOperationSerializer, \
    AboutUsSerializer, ServiceSerializer, ServiceImageSerializer
from service.models import Brand, ContactNumber, Address, Category, HoursOfOperation, \
    AboutUs, Service, ServiceImage

# Create your views here.

class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class ContactNumberView(viewsets.ModelViewSet):
    queryset = ContactNumber.objects.all()
    serializer_class = ContactNumberSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AboutUsView(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class HoursOfOperationView(viewsets.ModelViewSet):
    queryset = HoursOfOperation.objects.all()
    serializer_class = HoursOfOperationSerializer

class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceImageView(viewsets.ModelViewSet):
    queryset = ServiceImage.objects.all()
    serializer_class = ServiceImageSerializer
