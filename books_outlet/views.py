from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Books
# Create your views here.


def index(request):
    entire_books = Books.objects.all()
    return render(request, "books_outlet/books_list.html", {
        "books": entire_books
    })