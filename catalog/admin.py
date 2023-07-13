from django.contrib import admin

from catalog.models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_category')

@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_product', 'price_buy', 'category',)
    list_filter = ('category',)
    search_fields = ('name_product', 'description',)
