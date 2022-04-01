from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Collection
from .serializer import ProductSerializer, CollectionSerializer

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        query_set= Product.objects.select_related('collection').all()
        serializer=ProductSerializer(query_set, many=True, context={'request':request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        

@api_view(['GET','PUT','DELETE'])
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method =='GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method =='DELETE':
        if product.orderitems.count() > 0:
            return Response({'error':'Product cannot be deleted'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def collection_list(request):
    if request.method == 'GET':
        queryset = Collection.objects.annotate(products_count = Count('product')).all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view()    
def collection_detail(request, pk):
    return Response('ok')
    
