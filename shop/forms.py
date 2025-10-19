from .models import Product
from django.forms import ModelForm, TextInput, Select

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'category']
        widgets = {
        'title': TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product name',
            }
        ),
        'price': TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product price',
            }
        ),  
        'category': Select(
            attrs={
                'class': 'form-control',
            }
        )
}
