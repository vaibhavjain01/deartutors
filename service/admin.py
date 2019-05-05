from django.contrib import admin
from service.models import AboutUs, Brand, Image, ContactNumber, Address, \
    HoursOfOperation, Category, Service, ServiceImage

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc')

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'description')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_number', 'title', 'short_desc', 'long_desc', 'address',
                    'logo_image', 'web_page_logo')

class ContactNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'country_code', 'telephone')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'suit_num', 'floor_num', 'street_num', 'city', 'province', 'country', 'postal_code')

class HoursOfOperationAdmin(admin.ModelAdmin):
    list_display = ('id', 'day', 'start_time', 'end_time')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_desc', 'self_webpage_link', 'price', 'duration_in_mins',
        'duration_in_hours', 'main_pic', 'category')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')

admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Image)
admin.site.register(ContactNumber, ContactNumberAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(HoursOfOperation, HoursOfOperationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceImage)