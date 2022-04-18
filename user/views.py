import email
from hashlib import new
from rest_framework.response import Response
from rest_framework.decorators import api_view
from uritemplate import partial
from .serializers import CustomerSerializer
from .models import Customer

def checkCustomerByEmail(email):
    try:
        Customer.objects.get(email= email)
    except:
        return 0
    return 1 
def checkCustomerByPhone(phone):
    try:
        Customer.objects.get(phone= phone)
    except:
        return 0
    return 1
def checkCustomerById(id):
    try:
        Customer.objects.get(id= id)
    except:
        return 0
    return 1    
@api_view(["GET"])
def get_customer_by_id(request,id):
    customer = Customer.objects.get(id = id)
    serializer = CustomerSerializer(customer,many=False)
    return Response(serializer.data)

@api_view(["POST"])
def create_customer(request):
    if checkCustomerByEmail(request.data.get("email")) == 1:
        return Response({"message":"Email đã tồn tại","error":True})
    if checkCustomerByPhone(request.data.get("phone")) == 1:
        return Response({"message":"Số điện thoại đã tồn tại","error":True})
    serializer = CustomerSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Đăng ký thành công","error":False})
    return Response({"message":"Có lỗi trong quá trình đăng ký","error":True})
    

@api_view(["POST"])
def change_password(request):
    try:
        customer = Customer.objects.get(id = request.data.get("id"))
    except:
        return Response({"message":"Không tồn tại khách hàng","error":True})
    if customer.get_password() == request.data.get("oldpassword"):
        updateData = {"password" : request.data.get("newpassword")}
        newcustomer = CustomerSerializer(instance=customer,data= updateData ,partial = True)
        if newcustomer.is_valid():
            newcustomer.save()
            return Response({"message":"Đổi mật khẩu thành công","error":False})
        else:
            return Response({"message":"Có lỗi trong quá trình đổi mật khẩu","error":True})
    else:
        return Response({"message":"Mật khẩu cũ không chính xác","error":True})

@api_view(["POST"])
def change_info(request):
    try:
        customer = Customer.objects.get(id = request.data.get("id"))
    except:
        return Response({"message":"Không tồn tại khách hàng","error":True})
    newcustomer = CustomerSerializer(instance=customer,data = request.data)
    if newcustomer.is_valid():
        newcustomer.save()
        return  Response({"message":"Cập nhật thông tin thành công","error":False})
    else:
        return Response({"message":"Có lỗi trong quá trình cập nhật thông tin","error":True})