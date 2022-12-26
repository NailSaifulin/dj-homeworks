from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def books_catalog(request):
    template = 'base.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def show_book(request, pub_date):
    template = 'book.html'
    book_item = Book.objects.filter(pub_date=pub_date).first()
    paginator = Paginator(Book.objects.all(), 1)
    page = paginator.get_page(book_item.id)

    book_next = Book.objects.filter(id=book_item.id+1).first()
    book_previous = Book.objects.filter(id=book_item.id-1).first()
    # print(book_next.pub_date)
    context = {
        'book': book_item,
        'page': page,
        'book_next': book_next,
        'book_previous': book_previous
    }
    return render(request, template, context)