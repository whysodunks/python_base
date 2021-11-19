import logging

from django.db import transaction
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .logging_serializer import *

log = logging.getLogger(__name__)


@api_view(http_method_names=['POST'])
def save_logging(request):
    try:
        with transaction.atomic():
            return Response({"success": True, "message": "Nice"})

    except Exception as e:
        log.error(e, exc_info=True)
        return Response({"success": False, "message": str(e)})
