from django.views.generic import ListView
from products.models import Product

# Create your views here.
class ProductSearchListView(ListView):
    context_object_name = 'products'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q')
        if query is not None:
            return Product.objects.serachProducts(query)
        return Product.objects.getFeaturedProducts()
