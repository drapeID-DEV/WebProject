from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('profile/', views.user_profile, name='profile'),
    path('login', views.user_login, name='login'),
    path('register', views.user_reg, name='register')
]
