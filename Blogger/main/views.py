from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from blog.models import Post

# Create your views here.


def home_view(request:HttpRequest):

    blogs=Post.objects.all()


    return render(request,'main/index.html',{"blogs":blogs})
# Create your views here.
