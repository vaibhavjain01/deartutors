from django.shortcuts import render
from rest_framework import status, viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.core import serializers

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

class CategoryServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get(self, request, *args, **kwargs):
        categoryId = Category.objects.get(name=kwargs["category"])
        print(kwargs["category"], categoryId)
        rtList = Service.objects.all().filter(category=categoryId)
        rtJsonList = serializers.serialize('json', rtList)
        print(rtJsonList)
        return HttpResponse(rtJsonList, content_type='application/json')


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

class BrandLogoView(generics.RetrieveAPIView):
    model = Brand
    def get(self, request, *args, **kwargs):
        img = Brand.objects.get(id=1).logo_image
        return HttpResponse(img, content_type="image/png")

class BrandWebPageLogoView(generics.RetrieveAPIView):
    model = Brand
    def get(self, request, *args, **kwargs):
        img = Brand.objects.get(id=1).web_page_logo
        return HttpResponse(img, content_type="image/png")

class ServiceThumbView(generics.RetrieveAPIView):
    model = Service
    def get(self, request, *args, **kwargs):
        print(kwargs['img_name'])
        img = Service.objects.all().filter(main_pic__contains=kwargs['img_name'])[0].main_pic
        return HttpResponse(img, content_type="image/png")