from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('product-detail/<str:pk>', views.about_product),

    path('clients/', views.clients),
    path('contact/', views.contact),
    path('services/', views.services),





]