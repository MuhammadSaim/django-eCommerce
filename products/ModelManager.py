from django.db import models

class ProductManager(models.Manager):
    def getProducts(self):
        return self.get_queryset().filter(featured=False)

    def getFeaturedProducts(self):
        return self.get_queryset().filter(featured=True)