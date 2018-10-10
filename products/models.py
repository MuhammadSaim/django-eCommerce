import random,string,os
from django.db import models

def get_file_ext(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = ''.join([random.choice(string.ascii_lowercase) for i in range(16)])
    name, ext = get_file_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'products/{final_filename}'

# Create your models here.
class Product(models.Model):
    title           = models.CharField(max_length=225)
    slug            = models.SlugField(unique=True)
    description     = models.TextField()
    image           = models.ImageField(upload_to=upload_image_path)
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)

    def __str__(self):
        return self.title
