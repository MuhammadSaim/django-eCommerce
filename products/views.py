from django.views.generic import ListView, DetailView
from .models import Product
from django.shortcuts import render

# Create your views here.

class ProductListView(ListView):
    context_object_name = 'products'
    queryset = Product.objects.all()


class ProductDetailView(DetailView):
    context_object_name = 'product'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
