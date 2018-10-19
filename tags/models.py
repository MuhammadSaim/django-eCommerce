from django.db import models
from products.models import Product
from products.utils import unique_slug_generator
from django.db.models.signals import pre_save


class Tag(models.Model):
    title       = models.CharField(max_length=255)
    slug        = models.SlugField(unique=True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    products    = models.ManyToManyField(Product)

    def __str__(self):
        return self.title


def Tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(Tag_pre_save_receiver, sender=Tag)