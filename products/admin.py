from django.contrib import admin

# Register your models here.

from .models import Product, Supplier, AddTransaction

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['code', 'name', 'model', 'cost', 'selling_price', 'size', 'img']
    list_display = ['code', 'name','selling_price']
    search_fields = ['code', 'name', 'selling_price']


admin.site.register(Product, ProductAdmin)

admin.site.register(Supplier)


admin.site.register(AddTransaction)
