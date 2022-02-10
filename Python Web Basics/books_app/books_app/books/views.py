from django.shortcuts import render, redirect

# Create your views here.
from books_app.books.forms import BookForm, AuthorForm, StateFilterForm
from books_app.books.models import Book


def index(req):
    filter_form = StateFilterForm(req.GET)
    filter_form.is_valid()
    state = filter_form.cleaned_data['state']
    if state == 'all':
        books = Book.objects.all()
    # else:
    #     pass

    context = {
        'books': Book.objects.all(),
        'filter_form': filter_form,
    }
    return render(req, 'index.html', context=context)


def show_book_form(req, book_form, author_form, template_name):
    context = {
        'book_form': book_form,
        'author_form': author_form,
    }
    return render(req, template_name, context)


def save_book_from_from(request, book_form, author_form, template):
    if book_form.is_valid() and author_form.is_valid():
        author = author_form.save()
        book = book_form.save(commit=False)
        book.author = author
        book.save()
        return redirect('home page')
    return show_book_form(request, book_form, author_form, template)


def create_book(req):
    if req.method == 'GET':
        book_form = BookForm()
        author_form = AuthorForm()
        return show_book_form(req, book_form, author_form, 'create.html')
    else:
        book_form = BookForm(req.POST)
        author_form = AuthorForm(req.POST)
        return save_book_from_from(req, book_form, author_form, 'create.html')


def update_book(req, pk):
    book = Book.objects.get(pk=pk)
    if req.method == "GET":
        book_form = BookForm(initial=book.__dict__)
        author_form = AuthorForm(initial=book.author.__dict__)
        return show_book_form(req, book_form, author_form, 'edit.html')
    else:
        book_form = BookForm(req.POST, instance=book)
        author_form = AuthorForm(req.POST, instance=book.author)
        return save_book_from_from(req, book_form, author_form, 'edit.html')
