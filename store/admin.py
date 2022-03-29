from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
from . import models


# Register your models here.

class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','products_count']
    
    @admin.display(ordering='products_count')
    def products_count(self,collection):
        url = (reverse('admin:store_product_changelist') 
        + '?'
        + urlencode({
            'collection__id':str(collection.id)
        }))
        return format_html('<a href="{}">{}</a>',url,collection.products_count)
        
    
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
    list_display = ['first_name', 'last_name', 'membership','orders']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields=['first_name','last_name']
    def orders(self, customer):
        url = (reverse("admin:store_order_changelist")
        + '?'
        + urlencode({
            'customer__id':customer.id
        }))
        return format_html("<a href='{}'>{}</a>",url,f"{customer.order_count} Orders")

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            order_count=Count('order')
        )

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