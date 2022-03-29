from django.contrib import admin
from django.db.models import Count
from . import models


# Register your models here.

class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','products_count']
    
    @admin.display(ordering='products_count')
    def products_count(self,collection):
        return collection.products_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count = Count('product')           
        )

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status','inventory','collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related=['collection']
    ordering = ['title','inventory']
    
    def inventory_status(self, product):
        if product.inventory < 10:
            return "Low"
        return "Ok"
    
    def collection_title(self,product):
        return product.collection.title



class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','placed_at','customer_name']
    list_select_related=['customer']
    list_per_page = 10
    ordering=['id']

    def customer_name(self,order):
        return  f"{order.customer.first_name} {order.customer.last_name}"
         

admin.site.register(models.Collection,CollectionAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Order,OrderAdmin)