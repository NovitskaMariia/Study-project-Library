from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Author
from book.models import Book
from django.contrib import messages
from django.http import HttpResponseNotAllowed
from .forms import AuthorForm


def start_author(request):
    authors = Author.get_all()
    return render(request, 'author/start_author.html', {'authors': authors})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            if not all(form.cleaned_data.values()):
                return render(request, 'author/add_author.html', {'form': form, 'error': 'Please, fill in all fields.'})
            form.save()
            return redirect('start_author')
    else:
        form = AuthorForm()
    return render(request, 'author/add_author.html', {'form': form})

def remove_author(request, author_id):
    if request.method == 'POST':
        author = Author.get_by_id(author_id)

        if author:
            if not author.books.all():
                author.delete_by_id(author_id)
                messages.success(request, f'Author "{author.name}" has been removed.')
            else:
                messages.error(request, f'Author "{author.name}" has associated books and cannot be removed.')
        else:
            messages.error(request, 'Author not found.')

        return redirect('start_author')
    else:
        return HttpResponseNotAllowed(['POST'])