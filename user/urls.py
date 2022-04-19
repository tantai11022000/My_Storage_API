from django.urls import path
from . import views
urlpatterns = [
    path('login-customer',views.login_customer,name="login-customer"),
    path('detail-customer/<int:id>',views.get_customer_by_id,name="detail-customer"),
    path('create-customer',views.create_customer,name="create-customer"),
    path('change-password-customer',views.change_password,name="change-password-customer"),
    path('change-info-customer',views.change_info,name="change-info-customer"),
]