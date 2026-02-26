from typing import Any

from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Books
from django.views.generic import View, ListView, DetailView

# Create your views here.


class IndexView(ListView):
    model = Books
    template_name = "books_outlet/books_list.html"
    context_object_name = "books"
    ordering = "-rating"



class BookDetailsView(DetailView):
    model = Books
    template_name = "books_outlet/book_details.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        fav = request.session.get("fav_books")
        book = self.object.slug

        print(fav)
        if book in fav:
            context["is_fav"] = True
        else:
            context["is_fav"] = False
        return context


class FavoritView(View):
    def post(self, request):
        book_id = request.POST.get('review_id')
        the_book = Books.objects.get(pk=book_id)

        if not request.session["fav_books"]:
            request.session["fav_books"] = []
        
        request.session["fav_books"].append(the_book.slug)
        request.session.modified = True

        return redirect('book_info', slug=the_book.slug)