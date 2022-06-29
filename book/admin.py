from django.contrib import admin
from .models import Book
# Register your models here.


@admin.register(Book)
class UserAdmin(admin.ModelAdmin):
    list_display = ['isbn_number', 'book_name', 'author']