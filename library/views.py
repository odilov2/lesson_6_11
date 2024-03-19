from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin


class BookListView(LoginRequiredMixin, View):
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


class AddNewBookView(View):
    def get(self, request):
        return render(request, "library/add_new_book.html")


class BookDeleteView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        book.delete()
        return redirect("books")


class BookSettingsView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        # form = AddBookModelForm()
        context = {
            "book": book
        }
        return render(request, "library/settings_book.html", context)

    def post(self, request, id):
        # form = AddBookModelForm(data=request.POST)
        title = request.POST["title"]
        description = request.POST["description"]
        count = request.POST["count"]
        price = request.POST["price"]
        image = request.POST["image"]

        book = Book.objects.get(id=id)
        book.title = title
        book.description = description
        book.count = count
        book.price = price
        book.image = f"library/authors/{image}"

        book.save()

        return redirect("books")
