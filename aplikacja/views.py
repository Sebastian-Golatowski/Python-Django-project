from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Collection, Product
from tags.models import TaggedItem


# Create your views here.


def sey_hello(request):
    


    
    return render(request, "html.html", {'name': 'Ja'})
