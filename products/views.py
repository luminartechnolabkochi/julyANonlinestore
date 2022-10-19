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
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            Mobiles.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
#localhost:products/{id}
# get
class ProductDetailView(APIView):
    def get(self,request,*args,**kw):
        return Response(data="mobile detail")



       

    