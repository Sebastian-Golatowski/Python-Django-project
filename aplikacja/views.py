from django.db.models import Q, F
from django.shortcuts import render
from django.db.models import Value
from store.models import Product,Order


# Create your views here.


def sey_hello(request):
    result=Product.objects.annotate(pies=F('id')+F('collection_id'),malap=Value(15))
   

    
    return render(request, "html.html", {'name': 'Ja', 'result':result})
