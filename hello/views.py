from django.shortcuts import render
from django.http import HttpResponse
# from .models import Greeting
import requests
import os
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *
from .sportsSchedules import getBaseballSchedule
import datetime
from datetime import date
import json
import requests
from sportsipy.nba.schedule import Schedule as basketballSchedule
from sportsipy.nba.teams import Teams as basketballTeams
from sportsipy.nhl.teams import Teams as hockeyTeams
from sportsipy.nhl.teams import Schedule as hockeySchedule
from sportsipy.mlb.schedule import Schedule as baseballSchedule
from sportsipy.mlb.teams import Teams as baseballTeams
from .forms import BetForm

# Create your views here.
def index(request):
    return render(request, 'Home.html')


def home(request):
    return render(request, 'Home.html')

def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            print(username)
            print(raw_password)
            temp=Users(username=username, password=raw_password, balance=0)
            temp.save()

            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('Home.html')
    else:
        print("failed")
        form = UserCreationForm()

    return render(request, 'Sign Up.html', {'form': form})


def login_view(request):
    last_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in user
            user = form.get_user()
            last_login = User.objects.get(username=user).last_login  # Grab information from auth_user
            login(request, user)
            request.session.set_expiry(0)

            # Give user payout
            if last_login.date() < datetime.date.today():
                current_user = Users.objects.get(username=user)
                current_user.balance = current_user.balance + 1000
                current_user.save()
            return redirect('Home.html')
    else:
        form = AuthenticationForm()
    return render(request, 'Login.html', {'form': form})


def CSGO(request):
    gameData= Games.objects.all()

    form = BetForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            user_ID = request.user.id
            game_ID = form.cleaned_data['game_ID']
            date_placed = datetime.date.today()
            team_bet = form.cleaned_data['team_bet']
            bet_amount = form.cleaned_data['bet_amount']
            game = Games.objects.get(pk=game_ID)
            team1=game.team1
            team2=game.team2
            current_user = Users.objects.get(username=request.user.username)
            if (bet_amount < current_user.balance):
                current_user.balance = current_user.balance - bet_amount
                current_user.save()
                temp = Bets(user_ID=user_ID, game_ID=game_ID, date_placed=date_placed, bet_amount=bet_amount, team1=team1, team2=team2, team_bet=team_bet)
                temp.save()

    context = {
        'form':form,
        'gameData' : gameData
    }

    return render(request, 'CSGO.html', context)


def DOTA(request):
    gameData= Games.objects.all()

    form = BetForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            user_ID = request.user.id
            game_ID = form.cleaned_data['game_ID']
            date_placed = datetime.date.today()
            team_bet = form.cleaned_data['team_bet']
            bet_amount = form.cleaned_data['bet_amount']
            game = Games.objects.get(pk=game_ID)
            team1=game.team1
            team2=game.team2
            current_user = Users.objects.get(username=request.user.username)
            if (bet_amount < current_user.balance):
                current_user.balance = current_user.balance - bet_amount
                current_user.save()
                temp = Bets(user_ID=user_ID, game_ID=game_ID, date_placed=date_placed, bet_amount=bet_amount,
                            team1=team1, team2=team2, team_bet=team_bet)
                temp.save()

    context = {
        'form':form,
        'gameData' : gameData
    }

    return render(request, 'DOTA.html', context)

def player_rankings(request):
    playerData = DotaPlayerRanking.objects.all()


    context = {
        'playerData' : playerData,
    }

    return render(request, 'Player Rankings.html', context)

def League(request):
    gameData= Games.objects.all()

    form = BetForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            user_ID = request.user.id
            game_ID = form.cleaned_data['game_ID']
            date_placed = datetime.date.today()
            team_bet = form.cleaned_data['team_bet']
            bet_amount = form.cleaned_data['bet_amount']
            game = Games.objects.get(pk=game_ID)
            team1=game.team1
            team2=game.team2
            current_user = Users.objects.get(username=request.user.username)
            if (bet_amount < current_user.balance):
                current_user.balance = current_user.balance - bet_amount
                current_user.save()
                temp = Bets(user_ID=user_ID, game_ID=game_ID, date_placed=date_placed, bet_amount=bet_amount,
                            team1=team1, team2=team2, team_bet=team_bet)
                temp.save()

    context = {
        'form':form,
        'gameData' : gameData
    }

    return render(request, 'League.html', context)

def Hockey(request):
    gameData= Games.objects.all()

    form = BetForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            user_ID = request.user.id
            game_ID = form.cleaned_data['game_ID']
            date_placed = datetime.date.today()
            team_bet = form.cleaned_data['team_bet']
            bet_amount = form.cleaned_data['bet_amount']
            game = Games.objects.get(pk=game_ID)
            team1=game.team1
            team2=game.team2
            current_user = Users.objects.get(username=request.user.username)
            if (bet_amount < current_user.balance):
                current_user.balance = current_user.balance - bet_amount
                current_user.save()
                temp = Bets(user_ID=user_ID, game_ID=game_ID, date_placed=date_placed, bet_amount=bet_amount,
                            team1=team1, team2=team2, team_bet=team_bet)
                temp.save()

    context = {
        'form':form,
        'gameData' : gameData
    }

    return render(request, 'Hockey.html', context)

def Basketball(request):
    gameData= Games.objects.all()

    form = BetForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            user_ID = request.user.id
            game_ID = form.cleaned_data['game_ID']
            date_placed = datetime.date.today()
            team_bet = form.cleaned_data['team_bet']
            bet_amount = form.cleaned_data['bet_amount']
            game = Games.objects.get(pk=game_ID)
            team1=game.team1
            team2=game.team2
            current_user = Users.objects.get(username=request.user.username)
            if (bet_amount < current_user.balance):
                current_user.balance = current_user.balance - bet_amount
                current_user.save()
                temp = Bets(user_ID=user_ID, game_ID=game_ID, date_placed=date_placed, bet_amount=bet_amount,
                            team1=team1, team2=team2, team_bet=team_bet)
                temp.save()

    context = {
        'form':form,
        'gameData' : gameData
    }

    return render(request, 'Basketball.html', context)

def Baseball(request):
    gameData= Games.objects.all()

    form = BetForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            user_ID = request.user.id
            game_ID = form.cleaned_data['game_ID']
            date_placed = datetime.date.today()
            team_bet = form.cleaned_data['team_bet']
            bet_amount = form.cleaned_data['bet_amount']
            game = Games.objects.get(pk=game_ID)
            team1=game.team1
            team2=game.team2
            current_user = Users.objects.get(username=request.user.username)
            if (bet_amount < current_user.balance):
                current_user.balance = current_user.balance - bet_amount
                current_user.save()
                temp = Bets(user_ID=user_ID, game_ID=game_ID, date_placed=date_placed, bet_amount=bet_amount,
                            team1=team1, team2=team2, team_bet=team_bet)
                temp.save()

    context = {
        'form':form,
        'gameData' : gameData
    }

    return render(request, 'Baseball.html', context)



def eSports(request):
    return render(request, 'eSports.html')

#displays bet history of user (filtered by ID) after validating user login
def myBets(request):
    if request.user.is_authenticated:
        betData= Bets.objects.all()
        print(request.user.id)
    else:
        print("\n\nNOT LOGGED IN\n\n")

    context = {
        'betData' : betData
    }
    return render(request, 'My Bets.html', context)

def sports(request):
    return render(request, 'sports.html')
def rewards(request):
    return render(request, 'rewards.html')
def myProfile(request):
    print(request.user.username)
    if(request.user.is_authenticated):
        current_user = Users.objects.get(username=request.user.username)
        print(current_user)
        context = {
            'current_user' : current_user
        }
        return render(request, 'My Profile.html' , context)
    else:
        return render(request, 'My Profile.html')
def inventory(request):
    return render(request, 'inventory.html')





# this function is our current functional user signup page
def test(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            print(username)
            print(raw_password)
            temp=Users(username=username,password=raw_password)
            temp.save()


            return redirect('Home.html')
    else:
        print("failed")
        form = UserCreationForm()

    return render(request, 'test.html', {'form': form})

def bet_button(request):
    gameData= Games.objects.all()

    form = BetForm(request.POST or None)
    if form.is_valid():
        user_ID = 0
        game_ID = form.cleaned_data['game_ID']
        date_placed = datetime.date.today()
        team_bet = form.cleaned_data['team_bet']
        bet_amount = form.cleaned_data['bet_amount']
        game = Games.objects.get(pk=game_ID)
        team1=game.team1
        team2=game.team2
        temp = Bets(user_ID=user_ID, game_ID=game_ID, date_placed=date_placed, bet_amount=bet_amount, team1=team1, team2=team2, team_bet=team_bet)
        temp.save()

    context = {
        'form':form,
        'gameData' : gameData
    }

    return render(request, 'bet_button.html', context)



# Sean's function in trying to display betting history.
# Currently it doesnt work as I need to edit the html
# to display the proper parameters
def test_mybets(request):
    if request.user.is_authenticated:
        betData= Bets.objects.filter(id=request.user.id)
    else:
        print("\n\nNOT LOGGED IN\n\n")
        betData="None"

    context = {
        'betData' : betData
    }
    return render(request, 'test_mybets.html', context)





class GameData_Handler():

    def calculate_payout_esport(self):
        betData = Bets.objects.all()
        userData = Users.object.all()
        link_lol = 'https://api.pandascore.co/lol/matches/upcoming?token=fQNSOqsNLnSeovs8fk1mzbjPAsl9bYX68UBsm5hWpjIo21rk0cg'
        r_lol = requests.get(link_lol)
        data_lol = json.loads(r_lol.text)
        for game in data_lol:
            gameID = game['id']
            gameFinished = game['status']
            if (gameFinished == 'finished'):
                winnerData = game['winner']
                winner = winnerData['name']
                if(winner == None):
                    for bet in betData :
                        if(bet.game_ID == gameID):
                            bet.winloss = 0
                else:
                    for bet in betData:
                        if(bet.game_ID == gameID):
                            if(bet.team_bet == winner):
                                bet.winloss = bet.bet_amount
                                bet.result = True
                                for user in userData:
                                    if(bet.user_ID == user.id):
                                        user.balance += bet.bet_amount
                            else:
                                bet.winloss = -int(bet.bet_amount)
                                bet.result = False
                                for user in userData:
                                    if(bet.user_ID == user.id):
                                        user.balance -= bet.bet_amount

    def get_api_data(self):
        print("Getting API DATA")
        #Clear games data table
        Games.objects.all().delete()
        #Get updated data
        # Hockey Match data
        today = datetime.date.today()
        teams = hockeyTeams(year=2021)
        for team in teams:
            print("\nTeam 1: ", team.name)
            team_1 = team.name
            teamSchedule = hockeySchedule(team.abbreviation, year=2021)
            for game in teamSchedule:
                if (game.datetime.date() > today):
                    add_to_list = True
                    startTime = game.datetime
                    print(game.datetime)
                    team_2 = game.opponent_name
                    gameName = team_1 + " " + team_2 + " " + str(game.datetime.date())
                    # check for duplicate matches
                    for each in Games.objects.all():
                        if (each.team1 == team_2 and each.team2 == team_1 and each.time_data == startTime):
                            add_to_list = False
                    if (add_to_list != False):
                        print("\nTeam 2: ", team.name)
                        print("\nStarting time", startTime)
                        Game_data = Games(name=gameName, time_data=startTime, sport='Hockey', team1=team_1, team2=team_2)
                        Game_data.save()
                        print("\ndata added")
                    add_to_list = True

        today = datetime.date.today()
        teams = basketballTeams(year=2021)
        for team in teams:
            print("\nTeam 1: ", team.name)
            team_1 = team.name
            teamSchedule = basketballSchedule(team.abbreviation, year=2021)
            for game in teamSchedule:
                if (game.datetime.date() > today):
                    add_to_list = True
                    startTime = game.datetime
                    print(game.datetime)
                    team_2 = game.opponent_name
                    gameName = team_1 + " " + team_2 + " " + str(game.datetime.date())
                    # check for duplicate matches
                    for each in Games.objects.all():
                        if (each.team1 == team_2 and each.team2 == team_1 and each.time_data == startTime):
                            add_to_list = False
                    if (add_to_list != False):
                        print("\nTeam 2: ", team.name)
                        print("\nStarting time", startTime)
                        Game_data = Games(name=gameName, time_data=startTime, sport='BasketBall', team1=team_1, team2=team_2)
                        Game_data.save()
                        print("\ndata added")
                    add_to_list = True

        today = datetime.date.today()
        teams = baseballTeams(year=2021)
        for team in teams:
            print("\nTeam 1: ", team.name)
            team_1 = team.name
            teamSchedule = baseballSchedule(team.abbreviation, year=2021)
            for game in teamSchedule:
                if (game.datetime.date() > today):
                    add_to_list = True
                    startTime = game.datetime
                    print(game.datetime)
                    team_2 = game.opponent_abbr
                    gameName = team_1 + " " + team_2 + " " + str(game.datetime.date())
                    # check for duplicate matches
                    for each in Games.objects.all():
                        if (each.team1 == team_2 and each.team2 == team_1 and each.time_data == startTime):
                            add_to_list = False
                    if (add_to_list != False):
                        print("\nTeam 2: ", team.name)
                        print("\nStarting time", startTime)
                        Game_data = Games(name=gameName, time_data=startTime, sport='baseball', team1=team_1, team2=team_2)
                        Game_data.save()
                        print("\ndata added")
                    add_to_list = True


        # LOL match data
        link_lol = 'https://api.pandascore.co/lol/matches/upcoming?token=fQNSOqsNLnSeovs8fk1mzbjPAsl9bYX68UBsm5hWpjIo21rk0cg'
        r_lol = requests.get(link_lol)
        data_lol = json.loads(r_lol.text)
        print(data_lol[0])
        for game in data_lol:
            print("\n\nLOL")
            gameName = game['name']
            print("\nMatch name:", gameName)
            gameID = game['id']
            print("\nMatch ID:", gameID)
            gameFinished = game['status']
            print("\nMatch status", gameFinished)
            startTime = game['scheduled_at']
            startTime = startTime.split('T')
            startTime[1] = startTime[1].split('Z')[0]
            time = startTime[0] + " " + startTime[1]
            print("\nStarting time", startTime)
            teams = game['opponents']
            if (len(teams) == 2):
                team_1 = teams[0]['opponent']['name']
                print(team_1)
                team_2 = teams[1]['opponent']['name']
                print(team_2)
                Game_data = Games(name=gameName, time_data=time, sport='LOL', team1=team_1, team2=team_2, match_id=gameID)
                Game_data.save()
            print("\n")

        print("\nDONE WITH LOL")
        # Dota 2 Match data
        link_dota = 'https://api.pandascore.co/dota2/matches/upcoming?token=fQNSOqsNLnSeovs8fk1mzbjPAsl9bYX68UBsm5hWpjIo21rk0cg'
        r_dota = requests.get(link_dota)
        data_dota = json.loads(r_dota.text)
        print(data_dota[0])
        for game in data_dota:
            print("\ndota2")
            gameName = game['name']
            print("\nMatch name:", gameName)
            gameID = game['id']
            print("\nMatch ID:", gameID)
            gameFinished = game['status']
            print("\nMatch status", gameFinished)
            startTime = game['scheduled_at']
            startTime = startTime.split('T')
            startTime[1] = startTime[1].split('Z')[0]
            time=startTime[0] + " " + startTime[1]
            print("\nStarting time", startTime)
            teams = game['opponents']
            if (len(teams) == 2):
                team_1 = teams[0]['opponent']['name']
                print(team_1)
                team_2 = teams[1]['opponent']['name']
                print(team_2)
                Game_data = Games(name=gameName, time_data=time, sport='dota2', team1=team_1, team2=team_2 , match_id=gameID)
                Game_data.save()
            print("\n")

        print("\nDONE WITH DOTA2")

        # CSGO Match data
        link_CSGO = 'https://api.pandascore.co/csgo/matches/upcoming?token=fQNSOqsNLnSeovs8fk1mzbjPAsl9bYX68UBsm5hWpjIo21rk0cg'
        r_CSGO = requests.get(link_CSGO)
        data_CSGO = json.loads(r_CSGO.text)
        print(data_CSGO)
        for game in data_CSGO:
            print("\nCSGO")
            gameName = game['name']
            print("\nMatch name:", gameName)
            gameID = game['id']
            print("\nMatch ID:", gameID)
            gameFinished = game['status']
            print("\nMatch status", gameFinished)
            startTime = game['scheduled_at']
            startTime = startTime.split('T')
            startTime[1] = startTime[1].split('Z')[0]
            print("\nStarting time", startTime)
            teams = game['opponents']
            if (len(teams) == 2):
                team_1 = teams[0]['opponent']['name']
                print(team_1)
                team_2 = teams[1]['opponent']['name']
                print(team_2)
                Game_data = Games(name=gameName, time_data=time, sport='CSGO', team1=team_1, team2=team_2, match_id=gameID)
                Game_data.save()
            print("\n")
        print("\nDONE WITH CSGO")

        return

    def DotaRank(self):
        # DOTA Player data
        DotaPlayerRanking.objects.all().delete()
        link_players = 'https://api.opendota.com/api/rankings'
        r_players = requests.get(link_players)
        data_players = json.loads(r_players.text)
        print(data_players)
        players = data_players['rankings']
        for player in players:
            name = player['personaname']
            score = player['score']  # temporarily 1 for everyone, as getting this value isn't as simple as the rest
            steamid = player['account_id']
            avatar_link = player['avatar']
            player_data = DotaPlayerRanking(name=name, rank=score, steamid=steamid,avatar=avatar_link)
            player_data.save()
            print("added rank data")
            # ++count
        print("DONE WITH DOTA PLAYER RANKINGS")

        return
