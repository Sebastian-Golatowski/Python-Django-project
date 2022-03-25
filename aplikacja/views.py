from django.db.models import Q, F ,Func
from django.shortcuts import render
from django.db.models import Value
from django.db.models.functions import Concat
from store.models import Product,Order,Customer


# Create your views here.


def sey_hello(request):
    result=Customer.objects.annotate(full_name=Func(F('first_name'), Value(' '), F("last_name"),function='CONCAT'))
    result=Customer.objects.annotate(full_name=Concat(F('first_name'), Value(' '), F("last_name")))


    
    return render(request, "html.html", {'name': 'Ja', 'result':result})
