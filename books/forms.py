from django import forms

from books.models import BookModel


class BookModelForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'