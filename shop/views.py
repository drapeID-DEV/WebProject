from django.shortcuts import render, redirect 
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Category, Product
from .forms import ProductForm

# Create your views here.

def shop(request):
    products = list(Product.objects.values("id", "title", "price", "category"))  
    categories = list(Category.objects.values("id", "title"))
    context = {
        "products": products,
        "categories": categories
    }
    return render(request, "products.html", context)
 
def createProduct(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
        else:
            error = "Перевірте дані"

    form = ProductForm()
    data = {
        'form': form
    }
    return render(request, 'createProduct.html', data)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'detailView.html'
    context_object_name = 'product'

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'update.html'
    success_url = '/products'
    form_class = ProductForm

class ProductDeletelView(DeleteView):
    model = Product
    template_name = 'delete.html'
    context_object_name = 'product'
    success_url = '/products'
