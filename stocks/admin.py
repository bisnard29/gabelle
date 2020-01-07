from django.contrib import admin
from .models import Type, Product, Site, Order


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'product')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Order)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('product1', 'product2', 'site1', 'site2', 'quantity1', 'quantity2', 'type1', 'type2')
