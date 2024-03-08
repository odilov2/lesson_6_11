from django.shortcuts import render
from django.views import View
from .models import Book


class BookListView(View):
    def get(self, request):
        book = Book.objects.all()
        context = {
            "books": book
        }
        return render(request, 'library/book_list.html', context)

