from django.contrib import admin
from .models import Product, ProductCategory, Basket


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug', )
    prepopulated_fields = {
        'slug': ('name', )
    }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug', 'price', 'quantity', 'image', 'category')
    prepopulated_fields = {
        'slug': ('name', )
    }

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
