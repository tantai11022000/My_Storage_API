import os
from django.db import models

from My_Storage_API.settings import MEDIA_ROOT, MEDIA_URL


# Create your models here.




class TypeGoods(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

# locate img upload
def locate_img_upload(instance, filename):
    
    return os.path.join("goods-img/{}/{}".format(instance.codeGoods,filename))
def locate_barcode_img_upload(instance, filename):
    # filename = instance.barcode + "_" + filename
    return os.path.join("goods-img/{}/{}".format(instance.code,filename))
# Goods models


class Goods(models.Model):
    
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, unique=True)
    barcode = models.CharField(max_length=200, blank=True)
    barcode_img = models.ImageField(blank=True, null=True, upload_to=locate_barcode_img_upload)
    quantity = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    kind = models.ForeignKey(TypeGoods, on_delete=models.SET_NULL, null=True, blank=True)
    desc = models.TextField(blank=True)
    out_of_stock = models.BooleanField(default=False)
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    def __str__(self):
        return self.code

class ImgGoods(models.Model):
    img = models.ImageField(upload_to=locate_img_upload, blank=True, null=True)
    codeGoods = models.ForeignKey(Goods,on_delete=models.SET_NULL,null=True,blank=True,related_name="list_img")
    def __str__(self):
        return str(self.img)

    