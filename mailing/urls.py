from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from mailing.apps import MailingConfig
from mailing.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView
    # toggle_clients  # , toggle_clients_add
from mailing.views import MessageListView, MessageCreateView, MessageUpdateView, MessageDeleteView
from mailing.views import MailingSettingListView, MailingSettingCreateView, MailingSettingUpdateView, MailingSettingDeleteView, MailingClientListView

app_name = MailingConfig.name


urlpatterns = [
    path('', (ClientListView.as_view()), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/edit/<int:pk>/', ClientUpdateView.as_view(), name='client_edit'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

    path('message/', (MessageListView.as_view()), name='message_list'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/edit/<int:pk>/', MessageUpdateView.as_view(), name='message_edit'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),

    path('setting/', (MailingSettingListView.as_view()), name='setting_list'),
    path('setting/create/', MailingSettingCreateView.as_view(), name='setting_create'),
    path('setting/edit/<int:pk>/', MailingSettingUpdateView.as_view(), name='setting_edit'),
    path('setting/delete/<int:pk>/', MailingSettingDeleteView.as_view(), name='setting_delete'),
    path('setting/<int:pk_setting>/clients_list/edit', MailingClientListView.as_view(), name='mailing_client'),
    # path('setting/clients_list/save', toggle_clients, name='mailing_client_save'),
    # path('setting/<int:pk_setting>/clients_list/save', toggle_clients, name='mailing_client_save'),
    # path('setting/<int:pk_setting>/clients_list/add', toggle_clients_add, name='mailing_client_add'),
    # path('setting/<int:pk_setting>/clients_list/delete', toggle_clients_delete, name='mailing_client_delete'),

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