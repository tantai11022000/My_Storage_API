from pyexpat import model
from django.contrib import admin


from .models import Goods, TypeGoods,ImgGoods
# Register your models here.

class GoodsAdmin(admin.ModelAdmin):
    list_display = ["name","code","price"]
    model = Goods

class TypeGoodsAdmin(admin.ModelAdmin):
    list_display = ["name"]
    model = TypeGoods
class ImgGoodsAdmin(admin.ModelAdmin):
    list_display = ["id","img","codeGoods"]
    model = ImgGoods


admin.site.register(ImgGoods, ImgGoodsAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(TypeGoods, TypeGoodsAdmin)