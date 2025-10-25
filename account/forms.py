from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput

class UserRefistrationForm(forms.ModelForm):
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password')

        widgets = {
        'username': TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
            }
        ),
        'first_name': TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First name',
            }
        ),
        'email': TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }
        ),
        'password': PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }
        ),
        }
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwprds don\'t match")
        return cd['password2']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)