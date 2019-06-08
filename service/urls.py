from django.urls import path
from service import views
from django.contrib import admin

app_name = "service"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', admin.site.urls),
    path('brand/', views.BrandView.as_view({'get': 'list'})),
    path('address/', views.AddressView.as_view({'get': 'list'})),
    path('contact/', views.ContactNumberView.as_view({'get': 'list'})),
    path('categories/', views.CategoryView.as_view({'get': 'list'})),
    path('aboutus/', views.AboutUsView.as_view({'get': 'list'})),
    path('hoursofoperation/', views.HoursOfOperationView.as_view({'get': 'list'})),
    path('services/', views.ServiceView.as_view({'get': 'list'})),
    path('services/<str:category>', views.CategoryServiceView.as_view()),
    path('serviceimages/', views.ServiceImageView.as_view({'get': 'list'})),
    path('servicelist/', views.ServiceImageListView.as_view()),
    path('media/images/brand_logo/<str:img_name>', views.BrandLogoView.as_view()),
    path('media/images/brand_web_page_logo/<str:img_name>', views.BrandWebPageLogoView.as_view()),
    path('media/images/service/thumb/<str:img_name>', views.ServiceThumbView.as_view()),
    path(r'upload/', views.FileUploadView.as_view()),
    path('contactus/', views.ContactUsView.as_view()),
]