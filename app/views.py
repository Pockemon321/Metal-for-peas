from django.http import HttpResponse
from django.shortcuts import render, redirect
from Metal.settings import DOMAIN_URL
from django.views.decorators.csrf import csrf_exempt
from app.models import Product

# Create your views here.


@csrf_exempt
def index(request):

    context = {
        "DOMAIN_URL": DOMAIN_URL,
    }
    try:
        products = Product.objects.all()
        context.update({
            "products": products
        })
        return render(request, 'index.html', context)
    except Exception as e:
        return HttpResponse(f"<h1>Произошла ошибка: </h1> {e}")


def delivery(request):
    return render(request, 'delivery.html')


def about(request):
    return render(request, 'about.html')

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def edit_product(request, product_id):
    # Логика редактирования товара
    return redirect('index')  # Перенаправляем на главную страницу после редактирования

def delete_product(request, product_id):
    # Логика удаления товара
    return redirect('index')
