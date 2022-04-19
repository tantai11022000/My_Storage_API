from distutils.command.config import config
from os import access
import string
from urllib import response
import jwt
from rest_framework.response import Response
from rest_framework.decorators import api_view

from My_Storage_API.settings import SECRET_KEY, SIMPLE_JWT
import user
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework_simplejwt.tokens import RefreshToken

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
def checkToken(request,nameCookie):
    accessToken = request.COOKIES.get("access_token")
    refreshToken = request.COOKIES.get("refresh_token")
    try:
        return  jwt.decode(accessToken,key=SIMPLE_JWT['SIGNING_KEY'],algorithms=[SIMPLE_JWT['ALGORITHM']]).get(nameCookie)
    except:
        try:
            return  jwt.decode(refreshToken,key=SIMPLE_JWT['SIGNING_KEY'],algorithms=[SIMPLE_JWT['ALGORITHM']]).get(nameCookie)    
        except:
            return Response({"Message":"Hết hạn đăng nhập","error":True})
@api_view(["POST"])
def login_customer(request):
    try:
        customer = Customer.objects.get(email = request.data.get("email"),password = request.data.get("password"))
    except:
        return Response({"message":"Email hoặc mật khẩu không chính xác","error":False})
    refreshToken = RefreshToken.for_user(customer)
    dataCustomer = CustomerSerializer(customer)
    response = Response()
    response.set_cookie("access_token",refreshToken.access_token)
    response.set_cookie("refresh_token",refreshToken)
    response.data = {"message":"Đăng nhập thành công","error":True,
        "customerId": dataCustomer.data.get("id")}
    return response

@api_view(["GET"])
def get_customer_by_id(request,id):
    check = checkToken(request,"user_id")
    if check == id :
        try:
            customer = Customer.objects.get(id = id)
        except:
            return Response({"Message":"Không tồn tại khách hàng","error":True})
        serializer = CustomerSerializer(customer,many=False)
        return Response(serializer.data)
    return check

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
    check = checkToken(request,"user_id")
    if check == request.data.get("id"):
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
    return check

@api_view(["POST"])
def change_info(request):
    check = checkToken(request,"user_id")
    if check == request.data.get("id"):
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
    return check