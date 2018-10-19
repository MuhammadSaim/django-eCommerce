from django.db import models
from django.db.models import Q

class ProductQuerySet(models.query.QuerySet):
    def activeProducts(self):
        return self.filter(published=True)

    def getProducts(self):
        return self.filter(featured=False)

    def featuredProducts(self):
        return self.filter(featured=True)

    def searchProducts(self, query):
        lookups = (
                Q(title__icontains=query)       |
                Q(description__icontains=query) |
                Q(price__icontains=query)       |
                Q(tag__title__icontains=query)  
        )
        return self.activeProducts().filter(lookups).distinct()