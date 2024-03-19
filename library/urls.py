from django.urls import path
from .views import BookListView, BookDetailView, AddNewBookView, BookDeleteView, BookSettingsView

urlpatterns = [
    path("detail/<int:id>/", BookDetailView.as_view(), name='detail'),
    path('books/', BookListView.as_view(), name='books'),
    path('booksdelete/<int:id>/', BookDeleteView.as_view(), name='bookdelete'),
    path('booksettings/<int:id>/', BookSettingsView.as_view(), name='booksettings'),
    path('add_book/', AddNewBookView.as_view(), name='add_book'),
]
