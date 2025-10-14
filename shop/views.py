from django.shortcuts import render
from .models import Category, Product
from django.http import HttpResponse

# Create your views here.

def shop(request):
    products = list(Product.objects.values("title", "price", "category"))  
    categories = list(Category.objects.values("id", "title"))
    context = {
        "products": products,
        "categories": categories
    }
    return render(request, "shop.html", context)