from django.shortcuts import render
from blog.models import Blog

def home_view(request):

    blog = Blog.objects.all()
    return render(request, 'main/home.html',{"blog":blog})
