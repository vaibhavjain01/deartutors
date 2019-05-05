from rest_framework import serializers
from django.contrib.auth.models import User, Group
from service.models import  AboutUs, Brand, ContactNumber, Address, \
    HoursOfOperation, Category, Service, ServiceImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'desc')
        read_only_fields = fields

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'suit_num', 'floor_num', 'street_num', 'street_name', 'city', 'province', 'country', 'postal_code')
        read_only_fields = fields

class ContactNumberSerializer(serializers.ModelSerializer):
    #complete_telephone = serializers.SerializerMethodField()
    class Meta:
        model = ContactNumber
        fields = ('id', 'country_code', 'telephone', 'complete_telephone')
        read_only_fields = fields


class BrandSerializer(serializers.ModelSerializer):
    contact_number = serializers.SlugRelatedField(read_only=True, slug_field='complete_telephone')
    address = serializers.SlugRelatedField(read_only=True, slug_field='complete_address')
    logo_image_url = serializers.SerializerMethodField()
    web_page_logo_url = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = ('id', 'name', 'contact_number', 'title', 'short_desc', 'long_desc', 'address',
                    'logo_image_url', 'web_page_logo_url')
        read_only_fields = fields

    def get_logo_image_url(self, instance):
        request = self.context.get('request')
        if instance.logo_image and hasattr(instance.logo_image, 'url'):
            logo_url = instance.logo_image.url
            return request.build_absolute_uri(logo_url)
        else:
            return None

    def get_web_page_logo_url(self, instance):
        request = self.context.get('request')
        if instance.web_page_logo and hasattr(instance.web_page_logo, 'url'):
            logo_url = instance.web_page_logo.url
            return request.build_absolute_uri(logo_url)
        else:
            return None