from django.http import JsonResponse
import json



def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body) # string of json data -> python dict
    except:
        pass

    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    print(data)
    return JsonResponse(data)
