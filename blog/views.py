from django.shortcuts import render
from django.views import View

from .models import Blog, Comments


class BlogView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        context = {
            'blogs': blogs
        }
        return render(request, 'blogs.html', context)


class BlogDetailView(View):
    def get(self, request, id):
        blog = Blog.objects.get(id=id)
        return render(request, "blog_detail.html", {"blog": blog})

