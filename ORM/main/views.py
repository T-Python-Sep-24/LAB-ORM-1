from django.shortcuts import render
from blogs.models import Blog

def home_view(request):
    # Get all blogs
    blogs = Blog.objects.all()
    return render(request, 'main/blog.html', {"blogs": blogs})
