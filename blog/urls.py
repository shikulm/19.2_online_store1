from django.urls import path

from blog.apps import BlogConfig
# from catalog.views import home, contacts, catalog, category_catalog
# from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

from catalog.apps import CatalogConfig

app_name = BlogConfig.name

urlpatterns = [
    # path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    # path('blog/', BlogListView.as_view(), name='blog_list'),
    # path('view/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    # path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    # path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]