from django.shortcuts import render, HttpResponseRedirect
from .forms import BookManagementSystem
from .models import Book


# Create your views here.


# This function will Add/Show data.
def add_show(request):
    if request.method == 'POST':
        fm = BookManagementSystem(request.POST)
        if fm.is_valid():
            isbn_number = fm.cleaned_data.get('isbn_number')
            book_name = fm.cleaned_data.get('book_name')
            author = fm.cleaned_data.get('author')
            reg = Book(isbn_number=isbn_number,
                       book_name = book_name,
                       author = author)
            reg.save()
            fm = BookManagementSystem()

    else:
        fm = BookManagementSystem()
    stud = Book.objects.all()

    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})


# This function will Update/Edit data.
def update_data(request, id):
    if request.method == 'POST':
        pi = Book.objects.get(pk=id)
        fm = BookManagementSystem(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Book.objects.get(pk=id)
        fm = BookManagementSystem(instance=pi)
    return render(request, 'enroll/updatebook.html', {"form": fm})

#This function will delete Data.
def delete_data(request, id):
    if request.method == 'POST':
        pi = Book.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/')




