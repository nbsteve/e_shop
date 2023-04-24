from django.shortcuts import render
from .import models

# Create your views here.
def home(request):
    # Получить все продукты из базы
    all_products = models.Product.objects.all() #select * from products

    # Передать на Front часть
    context = {'products' : all_products}

    return render(request, 'index.html', context)

# Функция для отображения информации о конкретном продукте
def about_product(request, pk):
    # Получить конкретный продукт/данные из базы
    current_product = models.Product.objects.get(product_name=pk)
    context = {'product' : current_product}


    return render(request, 'about.html', context)



def clients(request):
    return render(request, 'clients.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')


