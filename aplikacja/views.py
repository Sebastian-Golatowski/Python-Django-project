from django.shortcuts import render

from store.models import Product


# Create your views here.


def sey_hello(request):
    x = Product.objects.values('title', 'collection__title')

    return render(request, "html.html", {'name': 'Ja', 'product': list(x)})
