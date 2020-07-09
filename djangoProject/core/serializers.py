from rest_framework import serializers
from .models import Compra

class CompraSerializer(serializers.Serializer):
    date = serializers.DateField()
    discount = serializers.DecimalField(max_digits=20, decimal_places=2)
    manufacturer_id = serializers.IntegerField()
    product = serializers.CharField(max_length=50, default='')
    product_id = serializers.IntegerField()
    quantity = serializers.DecimalField(max_digits=20, decimal_places=2)
    store_id = serializers.CharField(max_length=20, default='')
    total_value = serializers.DecimalField(max_digits=20, decimal_places=2)
    value = serializers.DecimalField(max_digits=20, decimal_places=2)

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Snippet.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance
