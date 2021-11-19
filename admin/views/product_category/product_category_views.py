import logging

from django.db import transaction
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .product_category_serializer import *

log = logging.getLogger(__name__)


@api_view(http_method_names=['GET'])
def get_product_category(request):
    try:
        with transaction.atomic():
            return Response({"success": True, "data": []})

    except Exception as e:
        log.error(e, exc_info=True)
        return Response({"success": False, "message": str(e)})
