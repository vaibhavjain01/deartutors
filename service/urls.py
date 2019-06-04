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
    path('serviceimages/', views.ServiceImageView.as_view({'get': 'list'})),
    path('servicelist/', views.ServiceImageListView.as_view()),
    path('media/images/brand_logo/<str:media_path>', views.MediaImageView.as_view()),
]