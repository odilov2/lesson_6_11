from django.contrib import admin
from .models import Book, BookRecord, Customer
from import_export.admin import ImportExportModelAdmin

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'role']
    list_display_links = ['first_name', 'last_name', 'role']
    search_fields = ['first_name', 'last_name']
    ordering = ['first_name']


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'count']
    list_display_links = ['title', 'description', 'price', 'count']
    search_fields = ['title', 'description']
    ordering = ['title']


@admin.register(BookRecord)
class BookRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'book', 'create_date', 'returned_date']
    list_display_links = ['customer', 'book', 'create_date', 'returned_date']
    autocomplete_fields = ['book', 'customer']
    search_fields = ['customer', 'book']
    ordering = ['-customer']
