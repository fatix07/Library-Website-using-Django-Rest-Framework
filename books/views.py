from django.shortcuts import render
from .models import Book
from django.views.generic import ListView,CreateView
class BookListView(ListView):
     model=Book
     template_name="book_list.html"
class BookCreateView(CreateView):
    model=Book
    template_name='books/book_form.html'
    fields=['title','subtitle','author','isbn']
    success_url='/'

# Create your views here.
