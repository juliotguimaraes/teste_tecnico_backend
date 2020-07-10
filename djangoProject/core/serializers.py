from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Compra

class CompraSerializer(ModelSerializer):
    date = serializers.DateField()
    discount = serializers.DecimalField(max_digits=20, decimal_places=2)
    manufacturer_id = serializers.IntegerField()
    product = serializers.CharField(max_length=50, default='')
    product_id = serializers.IntegerField()
    quantity = serializers.DecimalField(max_digits=20, decimal_places=2)
    store_id = serializers.CharField(max_length=20, default='')
    total_value = serializers.DecimalField(max_digits=20, decimal_places=2)
    value = serializers.DecimalField(max_digits=20, decimal_places=2)
    class Meta:
        model = Compra
        fields = (
            'date', 'discount', 'manufacturer_id', 'product', 'product_id', 'quantity', 'store_id', 'total_value', 'value'
        )
