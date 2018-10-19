from django.db import models
from .ProductQuerySet import ProductQuerySet

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self.db)

    def getProducts(self):
        return self.get_queryset().activeProducts().getProducts()

    def getFeaturedProducts(self):
        return self.get_queryset().activeProducts().featuredProducts()

    def serachProducts(self, query):
        return self.get_queryset().searchProducts(query)


