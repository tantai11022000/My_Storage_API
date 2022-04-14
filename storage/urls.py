from django.urls import path
from . import views
urlpatterns = [
    path('list-goods/<int:offset>/<int:limit>/',views.get_list_goods,name="list-goods")
]