from django.urls import path, include
from django.views import View
from . import views

urlpatterns = [
    path("products/",views.product_list),
    path("products/<int:id>/",views.product_detail),
    path("collections/",views.collections_list),
    path("collections/<int:id>",views.collection_detail)
]