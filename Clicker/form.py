from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Match, Player

# Create the form class.
class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ["name"]

class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = ["player_id", "score"]
