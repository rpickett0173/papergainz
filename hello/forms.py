from django import forms
from hello.models import Bets

# function for creating the entity that displays the game information
# and facilitates placing the bet
class BetForm(forms.ModelForm):
    class Meta:
        model = Bets
        fields = ['game_ID','team_bet','bet_amount']