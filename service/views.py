from django.shortcuts import render
from rest_framework import status, viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

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

class ServiceImageListView(generics.ListAPIView):
    model = ServiceImage
    serializer_class = ServiceImageSerializer

    def get_queryset(self, *args, **kwargs):
        service_query = self.request.GET.get('service_name')
        print("VJ", service_query)
        queryset = ServiceImage.objects.all()
        
        if service_query is not None:
            queryset = queryset.filter(service_name__name__icontains=service_query)
        return queryset

class MediaImageView(generics.RetrieveAPIView):
    model = Brand
    def get(self, request, *args, **kwargs):
        print("VJ A")
        print(request)
        print("VJ B")
        print(kwargs.keys())
        print("VJ C")
        print(kwargs["media_path"])
        img = Brand.objects.get(id=1).logo_image
        return HttpResponse(img, content_type="image/png")