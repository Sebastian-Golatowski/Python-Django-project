from django.shortcuts import render
from store.models import Product
from django.shortcuts import render

from store.models import Product


# Create your views here.


def sey_hello(request):
    x = Product.objects.filter(id__gt=90)
    
    return render(request, "html.html", {'name': 'Ja', 'product': list(x)})
