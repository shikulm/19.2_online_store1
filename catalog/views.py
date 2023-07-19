from django.shortcuts import render

from catalog.models import Product, Category


# Create your views here.

def home(request):
    context = {
        'title': 'Главная',
    }
    # print(Product.objects.all().order_by('-pk')[:5])
    return render(request, 'catalog/home.html', context)


def catalog(request):
    # print(Product.objects.all().order_by('-pk')[:5])
    category_list = Category.objects.all()
    products_list = Product.objects.all()
    context = {
        'category_list': category_list,
        'object_list': products_list,
        'title': 'Каталог',
        'category': ''
    }
    return render(request, 'catalog/catalog.html', context)


def category_catalog(request, pk):
    category_list = Category.objects.all()
    # print(Product.objects.all().order_by('-pk')[:5])
    products_list = Product.objects.filter(category=pk)
    context = {
        'category_list': category_list,
        'object_list': products_list,
        'title': 'Каталог',
        'category': Category.objects.get(pk=pk)
    }
    return render(request, 'catalog/catalog.html', context)


# def catalog(request):
#     # print(Product.objects.all().order_by('-pk')[:5])
#     products_list = Product.objects.all()
#     context = {
#         'object_list': products_list,
#         'title': 'Каталог',
#     }
#     return render(request, 'catalog/catalog.html', context)


def contacts(request):
    if request.method == "POST":
        print(request.encoding)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email} - {message}')
    context = {
            'title': 'Контакты',
        }
    return render(request, 'catalog/contacts.html', context)