from django.shortcuts import render
from django.db.models import Q
from store.models import  Customer, Product

# Create your views here.


def sey_hello(request):
    query_set = Product.objects.raw("SELECT * FROM store_Product ORDER BY title")

    for product in query_set:
        print(product.title)
    
    
    return  render(request,"html.html",{'name':'Ja','products':query_set})