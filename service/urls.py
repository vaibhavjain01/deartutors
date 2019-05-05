from django.urls import path
from service import views

app_name = "service"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', views.BrandView.as_view({
    'get': 'list'
    })),
]