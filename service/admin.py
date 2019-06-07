from django.contrib import admin
from service.models import AboutUs, Brand, ContactNumber, Address, \
    HoursOfOperation, Category, Service, ServiceImage, AppointmentRequest, \
    ContactMessage, TemporaryFileUpload

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_desc', 'long_desc')

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'short_description', 'long_description')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_number', 'title', 'short_desc', 'long_desc', 'address',
                    'logo_image', 'web_page_logo', 'email', 'facebook_url', 'twitter_url', 'linkedin_url')

class ContactNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'country_code', 'telephone')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'suit_num', 'floor_num', 'street_num', 'street_name', 'city', 'province', 
                    'country', 'postal_code')

class HoursOfOperationAdmin(admin.ModelAdmin):
    list_display = ('id', 'day', 'start_time', 'end_time')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_desc', 'self_webpage_link', 'price', 'duration_in_mins',
        'duration_in_hours', 'main_pic', 'category')

class ServiceImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_name', 'image')

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender_email', 'subject', 'msg', 'msg_time', 'file')

class AppointmentRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_name', 'request_date', 'request_time', 'request_duration')

class TemporaryFileUploadAdmin(admin.ModelAdmin):
    list_display = ('upload_id', 'file')

admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(ContactNumber, ContactNumberAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(HoursOfOperation, HoursOfOperationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceImage, ServiceImageAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(AppointmentRequest, AppointmentRequestAdmin)
admin.site.register(TemporaryFileUpload, TemporaryFileUploadAdmin)