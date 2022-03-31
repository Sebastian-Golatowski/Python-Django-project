from dataclasses import field
from decimal import Decimal
from store.models import Product, Collection
from rest_framework import serializers

class CollectionSerializer(serializers.Serializer):
    class Meta:
        model = Collection
        fields=['id','title']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=['id','title','unit_price','price_with_tax','collection']
    
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection = serializers.HyperlinkedRelatedField(
        queryset = Collection.objects.all(),
        view_name = 'collection-detail',
    )
    
    def calculate_tax(self, product):
        return round(product.unit_price * Decimal(1.1),2)