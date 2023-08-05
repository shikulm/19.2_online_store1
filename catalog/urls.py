from django.urls import path

# from catalog.views import home, contacts, catalog, category_catalog
from catalog.views import HomeTemplateView, ProductListView, ContactsCreateView, ProductCreateView, ProductDeleteView, \
    ProductUpdateView, ProductDetailView

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

# urlpatterns = [
#     path('', home, name='home'),
#     path('catalog/', catalog, name='catalog'),
#     path('<int:pk>/catalog/', category_catalog, name='category_catalog'),
#     path('contacts/', contacts, name='contacts'),
# ]


urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('catalog/create', ProductCreateView.as_view(), name='product_create'),
    path('catalog/edit/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    path('catalog/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('<int:pk>/catalog/', ProductListView.as_view(), name='category_catalog'),
    path('catalog/view/<int:pk>', ProductDetailView.as_view(), name='product_view'),
    path('contacts/create', ContactsCreateView.as_view(), name='contacts_create'),
]