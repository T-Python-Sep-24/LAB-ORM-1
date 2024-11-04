from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from postsApp.models import Post


# Create your views here.

def main_view(request: HttpRequest):
    # blogs = [
    #     {"title": "f", "img": ".jpg", "decs": "post etc"},
    #     {"title": "f", "img": ".jpg", "decs": "post etc"},
    #     {"title": "f", "img": ".jpg", "decs": "post etc"},
    #     {"title": "f", "img": ".jpg", "decs": "post etc"},
    # ]
    blogs = Post.objects.filter(is_published = True).order_by('-published_at')
    request = render(request, 'main.html', context={"blogs": blogs})
    return request
