from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.contrib.auth import get_user, logout
from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.decorators import login_required
from author.models import Author
from .forms import BookForm



def book(request):
    user = get_user(request)
    books_list = []
    books = Book.get_all()
    for book in books:
        authors = book.authors.all()
        authors_name = ', '.join([author.name for author in authors])
        books_list.append({
                "id": book.id, "name": book.name, "description": book.description, "count": book.count, "authors_name": authors_name
            })
    
    return render(request, 'book/book.html', {'books': books_list, 'active_page': 'books'})

   
def book_info(request):
    user = get_user(request)
    if request.method == "GET":
        book_id = request.GET.get('id')
        book = Book.get_by_id(book_id=book_id)
        authors = book.authors.all()
        authors_name = ', '.join([author.name for author in authors])
        return render(request, 'book/book_details.html', {'book': book, 'author': authors_name, 'role': user.role })
    
    
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            new_book = Book.create(**form.cleaned_data)
            return redirect('book')
        else:
            form = BookForm()
            return render(request, 'book/add_book.html', {'form': form, 'error': 'Your secret key incorrect'})
        
    form = BookForm()
    return render(request, 'book/add_book.html', {'form': form})
