from django.shortcuts import render,HttpResponse
from .models import Book

def index(request):
    try:
        books = Book.objects.all()
        book_found = True
    except Book.DoesNotExist:
        books = None
        book_found = False

    context = {
        'books': books,
        'book_found': book_found,
    }
   
    return render(request, 'library/index.html', context=context)
