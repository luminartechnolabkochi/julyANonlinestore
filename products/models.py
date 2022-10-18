from django.db import models

# Create your models here.
from django.db import models


# Create your models here.


class Mobiles(models.Model):
    name=models.CharField(max_length=200,unique=True)
    brand=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    specs=models.CharField(max_length=200)
    band=models.CharField(max_length=200)

    def __str__(self):
        return self.name

#orm query for  creating a resource
#ModelName.objects.create(field1=value1,field2=value2,,)
#Mobiles.objects.create(name="a52",brand="smasung",price=35000,specs="specifications",band="4G")
#orm query for fetching a specific record


# qs=ModelName.objects.get(id=2)

#filter()
# Mobiles.objects.filter(band="4G")
# field look_ups
# __lt <
#__gt >
#__lte <=
# __gte >=
#__iexact
#qs=Mobiles.objects.filter(price__lt=50000)
#qs=Mobiles.objects.filter(price__gt=35000)


# 33k -40k
#qs=Mobiles.objects.filter(price__gte=33000,price__lte=40000)

#all mobiles exclude samsung
#qs=Mobiles.objects.all().exclude(brand="samsung")



#4g mobiles
# qs=Mobiles.objects.filter(band__iexact="4g")

#update
# Mobiles.objects.filter(id=2).update(band="5G")

#delete
#Mobiles.objects.filter(id=4).delete()

# create=> create()
# list => all()
# filter=> filter()
#       > __gt
#       >= __gte
#       <  __lt
#       <= __lte
#        __iexact
#       __contains
#!= all().exclude()
# 
#qs=Mobiles.objects.all()


# url=localhost:8000/products
# method=GET

# url=localhost:8000/products?band=4g
# method=GET

# url=localhost:8000/products?band=4g&brand=samsung
# method=GET

# url=localhost:8000/products?price_gt=10000 & price__lt=20000
# method=GET

# url=localhost:8000/products/2/
# method=GET

#post,get,delete,put/patch
