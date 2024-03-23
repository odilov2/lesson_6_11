from django.contrib import admin
from .models import Blog, Comments

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'image', 'status', 'published_date', 'update_date',)


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'blog', 'create_date',)
