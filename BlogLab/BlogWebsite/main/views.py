from django.shortcuts import render ,redirect 
from django.http import HttpRequest , HttpResponse
from .models import Post
from django.utils import timezone
# Create your views here.

def home_view(request:HttpRequest):
    return render(request,"main/home.html")

def addPost_view (request : HttpRequest):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')  # Get the uploaded image
        post = Post(title=title, content=content, published_at=timezone.now())
        post.save()
        return redirect('main:home')  
    return render(request, 'main/addPost.html')