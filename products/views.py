from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Mobiles
from products.serializers import ProductSerializer


class ProductsView(APIView):
    def get(self,request,*args,**kw):
        qs=Mobiles.objects.all()
        serializer=ProductSerializer(qs,many=True)
        return Response(data=serializer.data)

       

    def post(self,request,*args,**kw):
        return Response(data="mobile create")

