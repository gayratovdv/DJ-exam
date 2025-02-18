from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.shortcuts import render, redirect

from users.forms import RegistrationForm, LoginForm


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()

            add_permission = Permission.objects.get(codename='add_bookmodel', content_type__app_label='books')
            change_permission = Permission.objects.get(codename='change_bookmodel', content_type__app_label='books')
            delete_permission = Permission.objects.get(codename='delete_bookmodel', content_type__app_label='books')

            user.user_permissions.add(add_permission, change_permission, delete_permission)

            login(request, user)
            return redirect('books:list')

    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('books:list')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})


def logout_view(request):
    logout(request)
    return redirect('users:login')