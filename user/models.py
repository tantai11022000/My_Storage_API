from django.db import models
class Customer(models.Model):
    
    email = models.EmailField(max_length=200,unique=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=250,blank=True)
    phone = models.CharField(max_length=13)
    ranking_discount = models.CharField(max_length=20, blank=True, default="basic")
    birthday = models.DateField(blank=True, null=True)
    password = models.CharField(max_length=32)

    def __str__(self):
        return "{} - {}".format(self.name,self.phone)
    def get_password(self):
        return self.password