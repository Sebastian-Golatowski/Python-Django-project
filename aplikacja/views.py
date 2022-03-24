from django.db.models import Q, F
from django.shortcuts import render
from store.models import Product,OrderItem


# Create your views here.


def sey_hello(request):
    query_set=Product.objects.values('title').filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

    # for product in query_set:
    #     print(product.title)

    return render(request, "html.html", {'name': 'Ja', 'products': query_set})
