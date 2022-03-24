from django.db.models import Q, F
from django.shortcuts import render
from store.models import Product,Order


# Create your views here.


def sey_hello(request):
    query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # for product in query_set:
    #     print(product.title)

    return render(request, "html.html", {'name': 'Ja', 'orders': query_set})
