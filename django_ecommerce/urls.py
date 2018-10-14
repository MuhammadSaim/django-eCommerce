from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from .views import home_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('products/', include('products.urls')),
    path('search/', include('search.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
