from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    context_object_name = 'products'
    queryset = Product.objects.getProducts()


class ProductDetailView(DetailView):
    context_object_name = 'product'
    queryset = Product.objects.getProducts()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FeaturedProductListView(ListView):
    context_object_name = 'products'
    queryset = Product.objects.getFeaturedProducts()



class FeaturedProductDetailView(DetailView):
    context_object_name = 'product'
    queryset = Product.objects.getFeaturedProducts()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
