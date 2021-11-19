from django.urls import path

from .views.product_category import product_category_views

urlpatterns = [
    path('product-category', product_category_views.get_product_category),
]