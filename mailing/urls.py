from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from mailing.apps import MailingConfig

app_name = MailingConfig.name


urlpatterns = [
    # path('', cache_page(60)(HomeTemplateView.as_view()), name='home'),
    # path('catalog/create', ProductCreateView.as_view(), name='product_create'),
    # path('catalog/edit/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    # path('catalog/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    # path('catalog/', ProductListView.as_view(), name='catalog'),
    # # path('catalog/', never_cache(ProductListView.as_view()), name='catalog'),
    # path('<int:pk>/catalog/', ProductListView.as_view(), name='category_catalog'),
    # path('catalog/view/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_view'),
    # path('contacts/create',  cache_page(60)(ContactsCreateView.as_view()), name='contacts_create'),
]