from django.contrib import admin

from catalog.models import Category, Product, Contacts, Shape, Version


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_category')

@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_product', 'price_buy', 'category',)
    list_filter = ('category',)
    search_fields = ('name_product', 'description',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email',)
    search_fields = ('name', 'email', 'message',)

@admin.register(Shape)
class ShapeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_shape',)
    search_fields = ('name_shape',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'name_version', 'weight', 'shape', 'is_actual',)
    list_filter = ('product', 'shape', 'is_actual',)
    search_fields = ('name_version', 'weight', 'shape', 'is_actual',)