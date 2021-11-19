from django.urls import path

from .views.logging import logging_views

urlpatterns = [
    path('product_category', logging_views.save_logging),
]
