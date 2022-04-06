from django.urls import path, include
from django.views import View
from . import views

urlpatterns = [
    path("products/",views.ProductList.as_view()),
    path("products/<int:id>/",views.ProductDetail.as_view()),
    path("collections/",views.collections_list),
    path("collections/<int:id>",views.collection_detail)
]