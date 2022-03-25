from django.shortcuts import render
from django.db.models import Value,Q, F ,Func,Count
from django.db.models.functions import Concat
from store.models import Product,Order,Customer


# Create your views here.


def sey_hello(request):
    result=Customer.objects.annotate(count_order=Count("order")).order_by('-count_order')



    
    return render(request, "html.html", {'name': 'Ja', 'result':result})
