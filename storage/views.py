
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import GoodsSerializer
from storage.models import Goods
@api_view(["GET"])
def get_list_goods(request,offset,limit):
    total = offset + limit
    listGoods = Goods.objects.all()[offset:total]
    serializers = GoodsSerializer(listGoods,many=True)
    return Response(serializers.data)

@api_view(["GET"])
def get_detail_good_by_code(request,code):
    good = Goods.objects.get(code = code)
    serializers = GoodsSerializer(good,many=False)
    return Response(serializers.data)