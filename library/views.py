from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Book


class BookListView(View):
    def get(self, request):
        search = request.GET.get('search')
        if not search:
            book = Book.objects.all()
            context = {
                "books": book
            }
            return render(request, 'library/book_list.html', context)
        else:
            book = Book.objects.filter(title__icontains=search)
            if not book:
                return HttpResponse("<h3>Ma`lumot mavjus emas</h3>")
            else:
                context = {
                    "books": book,
                    "search": search
                }
                return render(request, 'library/book_list.html', context)



class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        context = {
            "book": book
        }
        return render(request, "library/books_detail.html", context)
