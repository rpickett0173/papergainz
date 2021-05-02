from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    balance = models.PositiveIntegerField(default = 10000)
    def __str__(self):
        return self.username

class Games(models.Model):
    name = models.CharField(max_length=300)
    match_id = models.PositiveIntegerField(null=True)
    sport = models.CharField(max_length=300)
    time_data = models.DateTimeField()
    team1 = models.CharField(max_length=300)
    team1_odds = models.DecimalField(max_digits=3, decimal_places=2,default=.5)
    team1_amount = models.PositiveIntegerField(default=0)
    team2 = models.CharField(max_length=300)
    team2_odds = models.DecimalField(max_digits=3, decimal_places=2,default=.5)
    team2_amount = models.PositiveIntegerField(default=0)
    winner = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Rewards(models.Model):
    name = models.CharField(max_length=300)
    price = models.PositiveSmallIntegerField()
    reward_type = models.CharField(max_length=300)
    def __str__(self):
        return self.name

# Bets model records each and every bet placed, the associated user and game IDs,
# the date it was placed, details on the game (team1, team2), the team that
# the user bet on, the size of the bet, and the result of their bet (win=1, loss=0)
# and how much they won/loss.
class Bets(models.Model):
    user_ID = models.PositiveIntegerField()
    game_ID = models.PositiveIntegerField(null=True) # null=true allows for this value to be null in the db
    username = models.CharField(max_length=100, null=True)
    team1 = models.CharField(max_length=300, null=True)
    team2 = models.CharField(max_length=300, null=True)
    team_bet = models.CharField(max_length=300,null=True)
    date_placed = models.DateTimeField() #auto_now automatically makes this value the current time when the method is called
    bet_amount = models.PositiveIntegerField()
    result = models.BooleanField(null=True)
    winloss = models.IntegerField(null=True)
    def __str__(self):
        return str(self.user_ID)





class DotaPlayerRanking(models.Model):
    name = models.CharField(max_length=300)
    rank = models.PositiveIntegerField(blank=True, null=True)
    steamid = models.TextField(null=True)
    avatar = models.TextField(blank=True)
    def __str__(self):
        return self.name
