from django.shortcuts import render

from store.models import Product


# Create your views here.


def sey_hello(request):
    query_set = Product.objects.filter(id__range=(1, 4))

    for product in query_set:
        print(product.title)

    return render(request, "html.html", {'name': 'Ja', 'products': query_set})
