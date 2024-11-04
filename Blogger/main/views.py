from django.shortcuts import render, redirect
from django.http import HttpRequest
from post.models import Post

#Home page
def homeView(request: HttpRequest):
    #Get the list of posts
    posts = Post.objects.all()

    return render(request, 'main/home.html', context={'posts': posts})

#Mode change
def modeView(request: HttpRequest, mode):
    response = redirect(request.GET.get("next", "/"))
    
    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")
        
    return response

#Handling 404 and 500
def custom404(request, *args, **argv):
    response = render(request, "404.html", status=404)
    return response

def custom500(request, *args, **argv):
    response = render(request, "500.html", status=500)
    return response

