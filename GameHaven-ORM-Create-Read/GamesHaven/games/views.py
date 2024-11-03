from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Game

# Create your views here.

def create_game_view(request:HttpRequest):


    if request.method == "POST":
        new_game = Game(title=request.POST["title"], description=request.POST["description"], publisher=request.POST["publisher"], rating=request.POST["rating"], release_date=request.POST["release_date"])
        new_game.save()

    return render(request, "games/create.html")