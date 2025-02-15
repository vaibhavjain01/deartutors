from django.shortcuts import render
from rest_framework import status, viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.http import HttpResponse
from django.core import serializers
from uuid import uuid4
import json
from datetime import datetime

from service.serializers import BrandSerializer, ContactNumberSerializer, \
    AddressSerializer, CategorySerializer, HoursOfOperationSerializer, \
    AboutUsSerializer, ServiceSerializer, ServiceImageSerializer
from service.models import Brand, ContactNumber, Address, Category, HoursOfOperation, \
    AboutUs, Service, ServiceImage, TemporaryFileUpload, ContactMessage

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

class AboutUsImageView(generics.RetrieveAPIView):
    model = AboutUs
    def get(self, request, *args, **kwargs):
        print(kwargs['img_name'])
        img = AboutUs.objects.all().filter(image__contains=kwargs['img_name'])[0].image
        return HttpResponse(img, content_type="image/png")

class AboutUsResumeView(generics.RetrieveAPIView):
    model = AboutUs
    def get(self, request, *args, **kwargs):
        print(kwargs['file_name'])
        resume_pdf = AboutUs.objects.all().filter(resume_pdf__contains=kwargs['file_name'])[0].resume_pdf
        return HttpResponse(resume_pdf, content_type="application/pdf")

class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def put(self, request):
        print("put", request.data)
        return Response(status=204)

    def post(self, request):
        in_mem_file = request.data['filepond']
        temp_file_id = uuid4()
        temp_file_obj = TemporaryFileUpload(upload_id = temp_file_id,
                                            file = in_mem_file)
        temp_file_obj.save()
        return Response(temp_file_id, status=status.HTTP_200_OK)

    def delete(self, request):
        if type(request.data) == type(b''):
            request_data = request.data.decode('utf-8')
        else:
            request_data = request.data
        upload_id = request_data.strip()
        uploaded_file = TemporaryFileUpload.objects.get(upload_id=upload_id)
        uploaded_file.delete()
        return Response(upload_id, content_type="text/plain")

class ContactUsView(APIView):
    def post(self, request):
        try:
            post_data = json.loads(request.body.decode('utf-8'))
            message = post_data["message"]
            email = post_data["email"]
            subject = post_data["subject"]
            uploaded_file_ids = post_data["uploaded_file_ids"]
            uploaded_file_id = uploaded_file_ids[0]
            uploaded_file_id = uploaded_file_id[1:-1]
            print(email, subject, message, uploaded_file_id, uploaded_file_ids)
            uploaded_file = TemporaryFileUpload.objects.get(upload_id=uploaded_file_id)
            
            contact_us_obj = ContactMessage(subject = subject,
                                            msg = message,
                                            sender_email = email,
                                            msg_time = datetime.now(),
                                            file = uploaded_file.file)
            contact_us_obj.save()
            uploaded_file.delete()
            print(email, subject, message, uploaded_file_ids)
        except:
            print("Operation Failed", e)
            return Response(status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_200_OK)