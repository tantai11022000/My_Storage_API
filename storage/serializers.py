from dataclasses import fields
from rest_framework import serializers
from .models import Goods,TypeGoods,ImgGoods



class ImgGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgGoods
        fields = '__all__'
        


class TypeGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeGoods
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    kind = TypeGoodsSerializer()
    list_img = serializers.StringRelatedField(many=True)
    class Meta:
        model = Goods
        fields = '__all__'