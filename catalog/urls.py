from django.urls import path

from catalog.views import home, contacts, catalog

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('catalog/', catalog, name='catalog'),
    path('contacts/', contacts, name='contacts'),
]