from django.urls import path

from books.views import BookListView, BookDetailView, BookCreateView, BookDeleteView, BookUpdateView

app_name = 'books'

urlpatterns = [
    path('books/', BookListView.as_view(), name='list'),
    path('create/', BookCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='delete'),
]