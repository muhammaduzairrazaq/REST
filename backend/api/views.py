from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict


from products.models import Product



def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data)
        return JsonResponse(data)
    #     data = model_to_dict(model_data, fields=["id", "content", "price"])
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers= {"content-type":"application/json"})