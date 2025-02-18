from django.contrib import admin
from .models import UserModel


@admin.register(UserModel)
class UserModel(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
