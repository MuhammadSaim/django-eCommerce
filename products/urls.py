from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail_view'),
    path('featured/all/', FeaturedProductListView.as_view(), name='featured_product_view'),
    path('featured/<slug:slug>/', FeaturedProductDetailView.as_view(), name='featured_product_detail_view'),
]
