from django.shortcuts import render

from store.models import Product

# Create your views here.


def sey_hello(request):
    query_set = Product.objects.count()
    query_set.filter()

    for product in query_set:
        print(product)

    return  render(request,"html.html")