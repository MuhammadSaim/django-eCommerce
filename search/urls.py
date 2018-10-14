from django.urls import path
from .views import ProductSearchListView


urlpatterns = [
    path('', ProductSearchListView.as_view(), name="search_view"),
]