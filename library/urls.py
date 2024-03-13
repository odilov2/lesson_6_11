from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path("<int:id>/", BookDetailView.as_view(), name='detail'),
    path('books/', BookListView.as_view(), name='books'),
]
