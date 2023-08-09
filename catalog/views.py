from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

from catalog.models import Product, Category, Contacts, Version
from catalog.forms import ProductForm, VersionForm


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Главная',
    }


# def home(request):
#     context = {
#         'title': 'Главная',
#     }
#     # print(Product.objects.all().order_by('-pk')[:5])
#     return render(request, 'catalog/home.html', context)


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    extra_context = {
        'title': 'Каталог',
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        # Фильтруем при необходимости по категориям
        if self.kwargs.get('pk'):
            queryset = queryset.filter(category=self.kwargs.get('pk'))

        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['category_list'] = Category.objects.all()
        # context_data['category'] = ''
        context_data['category'] = Category.objects.get(pk=self.kwargs.get('pk')) if self.kwargs.get('pk') else ''

        return context_data


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # context_data['version_list'] = Version.objects.filter(product_id=self.object.pk)
        context_data['version_list'] = self.object.version_set.filter(is_actual=True)
        print(context_data['version_list'])

        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        versionformset = inlineformset_factory(Product, Version, VersionForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = versionformset(self.request.POST)
        else:
            context_data['formset'] = versionformset()

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        versionformset = inlineformset_factory(self.model, Version, VersionForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = versionformset(self.request.POST, instance = self.object)
        else:
            context_data['formset'] = versionformset(instance = self.object)

        return context_data
    
    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
            
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:catalog')



# def catalog(request):
#     # print(Product.objects.all().order_by('-pk')[:5])
#     category_list = Category.objects.all()
#     products_list = Product.objects.all()
#     context = {
#         'category_list': category_list,
#         'object_list': products_list,
#         'title': 'Каталог',
#         'category': ''
#     }
#     return render(request, 'catalog/product_list.html', context)


# def category_catalog(request, pk):
#     category_list = Category.objects.all()
#     # print(Product.objects.all().order_by('-pk')[:5])
#     products_list = Product.objects.filter(category=pk)
#     context = {
#         'category_list': category_list,
#         'object_list': products_list,
#         'title': 'Каталог',
#         'category': Category.objects.get(pk=pk)
#     }
#     return render(request, 'catalog/product_list.html', context)


# def catalog(request):
#     # print(Product.objects.all().order_by('-pk')[:5])
#     products_list = Product.objects.all()
#     context = {
#         'object_list': products_list,
#         'title': 'Каталог',
#     }
#     return render(request, 'catalog/product_list.html', context)


class ContactsCreateView(CreateView):
    model = Contacts
    # template_name = 'catalog/contacts_form.html'
    fields = ('name', 'email', 'message')
    success_url = reverse_lazy('catalog:contacts_create')

    extra_context = {
        'title': 'Контакты',
    }

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            print(request.encoding)
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            print(f'{name} ({email} - {message}')

        return super().post(request, *args, **kwargs)

# def contacts(request):
#     if request.method == "POST":
#         print(request.encoding)
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'{name} ({email} - {message}')
#     context = {
#             'title': 'Контакты',
#         }
#     return render(request, 'catalog/contacts_form.html', context)
