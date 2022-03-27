from django.db import connection
from django.shortcuts import render


# Create your views here.


def sey_hello(request):
    with connection.cursor() as cursor:
        x = cursor.execute("SELECT * FROM store_product")

    return render(request, "html.html", {'name': 'Ja'})
