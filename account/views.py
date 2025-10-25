from django.shortcuts import render, redirect
from account.forms import UserLoginForm, UserRefistrationForm
from django.contrib.auth import authenticate, login

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
                    return redirect("profile/")
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

def user_reg(request):
    if request.method == "POST":
        form = UserRefistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user = form.save()
            return redirect("/products")
    else:
        form = UserRefistrationForm()
    return render(request, "register.html", {'form': form})
