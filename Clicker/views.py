from django.shortcuts import render

from Clicker.form import PlayerForm
from Clicker.models import Player

# Create your views here.

def index(request):
    pack = {"player_id": None, "form": None}
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
        players = Player.objects.all()
        player_id = 0
        pack["player_id"] = player_id
    else:
        form = PlayerForm()
        pack["form"] = form
    return render(request, "index.html", pack)
