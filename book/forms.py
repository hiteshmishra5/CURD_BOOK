from django.core import validators
from django import forms
from .models import Book


class BookManagementSystem(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn_number', 'book_name', 'author']
        widgets = {
            'isbn_number': forms.TextInput(attrs={'class': 'form-control'}),
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }