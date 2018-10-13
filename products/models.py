from django.db import models
from .ModelManager import ProductManager
from .utils import upload_image_path


# Create your models here.
class Product(models.Model):
    title           = models.CharField(max_length=225)
    slug            = models.SlugField(unique=True)
    description     = models.TextField()
    image           = models.ImageField(upload_to=upload_image_path)
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    featured        = models.BooleanField(default=False)
    published       = models.BooleanField(default=True)

    objects = ProductManager()
    def __str__(self):
        return self.title
