from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    data = request.data
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
        return Response(data)
