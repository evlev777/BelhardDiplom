from django.urls import path
from .views import IndexView, ProductListView

app_name = 'products'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('catalog/', ProductListView.as_view(), name='catalog'),
]