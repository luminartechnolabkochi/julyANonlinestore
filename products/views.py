from http import server
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Mobiles
from products.serializers import ProductSerializer


class ProductsView(APIView):
    def get(self,request,*args,**kw):
        
        qs=Mobiles.objects.all()
        if "brand" in request.query_params:
            qs=qs.filter(brand=request.query_params.get("brand"))
        if "band" in request.query_params:
            qs=qs.filter(band=request.query_params.get("band"))
        


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
        id=kw.get("id")
        qs=Mobiles.objects.filter(id=id)
        serilizer=ProductSerializer(qs,many=True)
        return Response(data=serilizer.data)
        
    def delete(self,request,*args,**kw):
        id=kw.get("id")
        Mobiles.objects.filter(id=id).delete()
        return Response(data="deleted")
    

    def put(self,request,*args,**kw):
        id=kw.get("id")
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            Mobiles.objects.filter(id=id).update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

