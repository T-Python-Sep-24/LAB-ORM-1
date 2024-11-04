from django.shortcuts import render
from .models import Main

def view_home(request):
    return render(request, 'main/blog.html')

def create_blog(request):
    if request.method == "POST":
        new_blog = Main(
            title=request.POST["title"],
            content=request.POST["content"]
        )
        new_blog.save()

    return render(request, 'main/create.html')