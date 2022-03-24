from django.db.models import Q
from django.shortcuts import render
from store.models import Product


# Create your views here.


def sey_hello(request):
    query_set = Product.objects.filter((Q(id__gt=14) | Q(inventory__lt=10)) & ~Q(unit_price__lt=20))

    for product in query_set:
        print(product.title)

    return render(request, "html.html", {'name': 'Ja', 'products': query_set})
