from django.shortcuts import render

from catalog.models import Product


# Create your views here.

def home(request):
    context = {
        'title': 'Главная',
    }
    # print(Product.objects.all().order_by('-pk')[:5])
    return render(request, 'catalog/home.html', context)


def catalog(request):
    # print(Product.objects.all().order_by('-pk')[:5])
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Каталог',
    }
    return render(request, 'catalog/catalog.html', context)


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