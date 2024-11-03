from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

def main_view(request:HttpRequest):

    return render(request, "main/home.html")



def new_posts_view(request:HttpRequest):

    return render(request, "main/new_post.html")

