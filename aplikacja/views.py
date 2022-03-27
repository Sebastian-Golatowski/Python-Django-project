from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.db import connection
from store.models import Collection, Product
from tags.models import TaggedItem


# Create your views here.


def sey_hello(request):
    with connection.cursor() as cursor:
        x = cursor.execute("SELECT * FROM store_product")

    
    return render(request, "html.html", {'name': 'Ja'})
