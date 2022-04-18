from pyexpat import model
from django.contrib import admin


from .models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id","name","email"]
    model = Customer


admin.site.register(Customer, CustomerAdmin)