from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from books.forms import BookModelForm
from books.models import BookModel, AuthorModel


class BookListView(ListView):
    model = BookModel
    queryset = BookModel.objects.order_by('-pk')
    template_name = 'index.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = BookModel
    template_name = 'detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = BookModel
    form_class = BookModelForm
    template_name = 'book_create.html'

    # permissions
    permission_required = 'books.add_bookmodel'
    login_url = 'users:login'
    raise_exception = True

    # success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(BookCreateView, self).get_context_data(**kwargs)
        context['authors'] = AuthorModel.objects.all()
        return context

    def get_success_url(self):
        return reverse('books:list')


class BookUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    queryset = BookModel.objects.all()
    form_class = BookModelForm
    template_name = 'book_update.html'
    success_url = '/'

    # permissions
    permission_required = 'books.change_bookmodel'
    login_url = 'users:login'  # Agar login qilmagan bo'lsa shu url ga o'tqazib yuboradi
    raise_exception = True

    # def get_success_url(self):
    #     return reverse('books:list')


class BookDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    model = BookModel
    template_name = 'book_delete.html'

    # permissions
    login_url = 'users:login'
    permission_required = 'books.delete_bookmodel'
    raise_exception = True

    # success_url = '/'

    def get_success_url(self):
        return reverse('books:list')