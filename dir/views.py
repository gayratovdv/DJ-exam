from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Item
from .forms import ItemForm, UserRegistrationForm


@login_required
def item_list(request):
    items = Item.objects.filter(user=request.user)
    paginator = Paginator(items, 10)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})


@login_required
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('dir:item_list')
    else:
        form = ItemForm()
    return render(request, 'create.html', {'form': form})


@login_required
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dir:item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'update.html', {'form': form, 'item': item})


@login_required
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk, user=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('dir:item_list')
    return render(request, 'delete.html', {'item': item})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dir:item_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dir:item_list')
        else:
            error_message = "Invalid username or password"
    else:
        error_message = ""
    return render(request, 'login.html', {'error_message': error_message})


@login_required
def user_logout(request):
    logout(request)
    return redirect('dir:login')
