from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, BlogListView_published
# from catalog.views import home, contacts, catalog, category_catalog
# from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

from catalog.apps import CatalogConfig

app_name = BlogConfig.name




urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('', BlogListView_published.as_view(), name='list'),
    path('all/', BlogListView.as_view(), name='list_all'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]