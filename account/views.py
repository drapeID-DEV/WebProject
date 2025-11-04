from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site

from .forms import UserRegistrationForm, UserLoginForm

def user_profile(request):
    return render(request, "profile.html")

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'], password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/account/profile")
                else:
                    message = "Account is disabled"
                    return render(request, "authInfo.html", {'message': message})
            else:
                message = "Invalid login"
                return render(request, "authInfo.html", {'message': message})
    else:
        form = UserLoginForm()
        context = {
            'title': 'Authentication',
            'form': form
        }
        return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect("/products")

def user_reg(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.set_password(form.cleaned_data['password'])
            user.save()
            current_site = get_current_site(request)
            subject = 'Підтвердження реєстрації'
            message = render_to_string('activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            send_mail(subject, message, 'admin@mysite.com', [user.email])

            messages.info(request, 'На вашу пошту надіслано лист із підтвердженням.')
            return redirect('account:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Ваш акаунт активовано! Тепер ви можете увійти.')
        return redirect('account:login')
    else:
        messages.error(request, 'Недійсне або прострочене посилання активації.')
        return redirect('register')