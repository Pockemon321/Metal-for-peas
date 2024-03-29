from django.contrib import admin
from django.urls import path, include
from app.views import *
from . import views

urlpatterns = [
    path('', index),
    path('delivery/', delivery),
    path('about/', about),
    path('product/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'),
]
