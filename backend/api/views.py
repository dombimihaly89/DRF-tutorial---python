import json
# from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer
# from django.forms.models import model_to_dict

# def api_home(request, *args, **kwargs):
#     # request -> HttpRequest -> Django
#     # print(dir(request)) dir returns all of the attributes and methods from any object
#     # request.body
#     print(type(request.GET)) # URL query params
#     print(request.POST)
#     body = request.body # byte string of JSON data. Bytes type
#     request
#     print(type(body))

#     data = {}
#     try:
#         data = json.loads(body) # string of JSON data -> Python Dict
#     except:
#         pass

#     print(data.keys())
#     print(type(request.headers))
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    '''
    DRF API View
    '''
    instance = Product.objects.all().order_by("?").first() # This gives back a random object from the Product table
    data = {}
    if instance:
        # data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
        data = ProductSerializer(instance).data
    return Response(data)

@api_view(['POST'])
def api_home_post(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    data = {}
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(f'instance : {instance}')
        data = serializer.data
    return Response(data)