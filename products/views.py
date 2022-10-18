from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# api
# list
# create
# details
# update
# delete

# localhost:8000/products/
# method:get

# localhost:8000/products/
# method:post
#data={"name":"a6","brand":"smasung","price":23000,"specs":"speci","band":"4G"}
class ProductsView(APIView):
    def get(self,request,*args,**kw):
        return Response(data="list of all mobiles")

    def post(self,request,*args,**kw):
        return Response(data="mobile create")

