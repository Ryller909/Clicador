from django.shortcuts import render, redirect

from Clicker.form import MatchForm, PlayerForm
from Clicker.models import Player

# Create your views here.

def index(request):
    pack = {"player_id": None, "form": None}
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
        pack["player_name"] = form["name"]
    else:
        form = PlayerForm()
        pack["form"] = form
    return render(request, "index.html", pack)

def save(request):
    if request.method == "POST" :
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
        print(form["player_id"])
        print(form["score"])
    return redirect("index")
