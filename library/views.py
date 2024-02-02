from django.shortcuts import render,HttpResponse
from django.db.models import Q
from .models import Book
from .forms import BookSearchForm


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

def book_search(request):
    search_form = BookSearchForm(request.GET)
    find_books = []
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        if query:
            # find_books = Book.objects.filter(title__contains=query)
            find_books = Book.objects.filter(
                Q(title__icontains=query) | Q(author__name__icontains=query)
                ) #search just from title of book

    context = {
        'search_form': search_form,
        'find_books': find_books,
    }        

    return render(request,'library/search.html', context=context )        
