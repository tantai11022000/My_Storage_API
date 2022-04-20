from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import GoodsSerializer, ImgGoodsSerializer
from storage.models import Goods, ImgGoods
from django.db.models import Q
from functools import reduce
from operator import or_
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from My_Storage_API.settings import BASE_DIR, MEDIA_ROOT


categories_param = openapi.Parameter('categories', openapi.IN_QUERY, description="String", type=openapi.TYPE_STRING)
colors_param = openapi.Parameter('colors', openapi.IN_QUERY, description="String", type=openapi.TYPE_STRING)
@swagger_auto_schema(method="GET",manual_parameters= [categories_param,colors_param])
@api_view(["GET"])
def get_list_goods(request,offset,limit):
    total = offset + limit
    try:
        categories = request.GET["categories"]
        colors = request.GET["colors"]
    except:
        listGoods = Goods.objects.all()[offset:total]
        serializers = GoodsSerializer(listGoods,many=True)
        return Response(serializers.data)
    amountCategories = 0
    amountColors = 0
    if (categories != ""):
        listCategories = categories.split(",")
        amountCategories= len(listCategories)
    if (colors != ""):
        listColors = colors.split(",")
        amountColors = len(listColors)
    if(amountCategories == 0 and amountColors == 0):
        listGoods = Goods.objects.all()[offset:total]
    elif (amountColors == 0 and amountCategories != 0):
        listGoods = Goods.objects.filter(kind__in=listCategories)[offset:total]
    else:
        colorCritical = reduce(or_, (Q(color__contains=color) for color in listColors))
        print(colorCritical)
        if (amountColors != 0 and amountCategories == 0):
            listGoods = Goods.objects.filter(colorCritical)[offset:total]
        else:    
            listGoods = Goods.objects.filter(kind__in=listCategories).filter(colorCritical)[offset:total]
    serializers = GoodsSerializer(listGoods,many=True)
    return Response(serializers.data)

@api_view(["GET"])
def get_detail_good_by_code(request,code):
    good = Goods.objects.get(code = code)
    serializers = GoodsSerializer(good,many=False)
    return Response(serializers.data)