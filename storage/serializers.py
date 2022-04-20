from pkg_resources import require
from rest_framework import serializers
from .models import Goods,TypeGoods,ImgGoods


class ImgGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgGoods
        fields = ["id","img"]
        


class TypeGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeGoods
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    kind = TypeGoodsSerializer()
    list_img = ImgGoodsSerializer(many=True)
    class Meta:
        model = Goods
        fields = '__all__'