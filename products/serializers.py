from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    brand=serializers.CharField()
    price=serializers.IntegerField()
    specs=serializers.CharField()
    band=serializers.CharField()
    