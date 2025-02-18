from django.contrib import admin
from .models import AuthorModel, BookModel


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'pseudo_name', 'age')


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'discount')
    list_filter = ('author',)
    search_fields = ('title', 'author__name', 'author__surname')
