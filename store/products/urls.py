from django.urls import path
from .views import index, products

urlpatterns = [
    path('', index, name='index'),
    path('catalog/', products, name='catalog'),
]