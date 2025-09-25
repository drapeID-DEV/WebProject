from django.shortcuts import render
from .models import Category
from django.http import HttpResponse

# Create your views here.

def index(request):
    categories = Category.objects.all()
    output = ''
    for category in categories:
        output += f'<h2>{category.title}</h2><br>'

    return HttpResponse(output)