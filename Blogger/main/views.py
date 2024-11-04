from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from blog.models import Blog

def home_view(request: HttpRequest):
    blog = Blog.objects.all()
    return render(request, "main/home.html", {"blog": blog})

