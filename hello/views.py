from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *
from .sportsSchedules import getBaseballSchedule
import datetime
from datetime import timedelta
import json
import requests
from sportsipy.nba.schedule import Schedule as basketballSchedule
from sportsipy.nba.teams import Teams as basketballTeams
from sportsipy.nhl.teams import Teams as hockeyTeams
from sportsipy.nhl.teams import Schedule as hockeySchedule
from sportsipy.mlb.schedule import Schedule as baseballSchedule
from sportsipy.mlb.teams import Teams as baseballTeams
from .forms import BetForm

############################# VIEWS #############################

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
            temp=Users(username=username, password=raw_password, balance=10000)
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
            print(user)
            # Give user payout

            if(last_login != None):
                if (last_login.date() < datetime.date.today()):
                    current_user = Users.objects.get(username=user)
                    current_user.balance = current_user.balance + 1000
                    current_user.save()
            else:
                current_user = Users.objects.get(username=user)
                current_user.balance = current_user.balance + 1000
                current_user.save()
            return redirect('Home.html')
    else:
        form = AuthenticationForm()
    return render(request, 'Login.html', {'form': form})

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

#displays bet history of user (filtered by ID) after validating user login
def myBets(request):
    if request.user.is_authenticated:
        betData = Bets.objects.all()
        print(request.user.id)
        context = {
            'betData' : betData
        }
        return render(request, 'My Bets.html', context)

    return render(request, 'My Bets.html')




def FAQ(request):
    return render(request, 'FAQ.html')


def eSports(request):
    return render(request, 'eSports.html')


def CSGO(request):
    gameData= Games.objects.all()

    form = BetForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            user_ID = request.user.id
            game_ID = form.cleaned_data['game_ID']
            date_placed = datetime.datetime.today()
            team_bet = form.cleaned_data['team_bet']
            bet_amount = form.cleaned_data['bet_amount']
            game = Games.objects.get(match_id=game_ID)
            team1=game.team1
            team2=game.team2
            current_user = Users.objects.get(username=request.user.username)
            if (bet_amount < current_user.balance):
                current_user.balance = current_user.balance - bet_amount
                current_user.save()
                temp = Bets(user_ID=user_ID, game_ID=game_ID, date_placed=date_placed, bet_amount=bet_amount, team1=team1, team2=team2, team_bet=team_bet,username= current_user)
                temp.save()

                #updating match odds
                #GameData_Handler.updateOdds(game_ID, team_bet, bet_amount)

    context = {
        'form':form,
        'gameData' : gameData
    }

    return render(request, 'CSGO.html', context)


def League(request):
    gameData= Games.objects.all()

    form = BetForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            user_ID = request.user.id
            game_ID = form.cleaned_data['game_ID']
            date_placed = datetime.datetime.today()
            team_bet = form.cleaned_data['team_bet']
            bet_amount = form.cleaned_data['bet_amount']
            game = Games.objects.get(match_id=game_ID)
            team1=game.team1
            team2=game.team2
            current_user = Users.objects.get(username=request.user.username)
            if (bet_amount < current_user.balance):
                current_user.balance = current_user.balance - bet_amount
                current_user.save()
                temp = Bets(user_ID=user_ID, game_ID=game_ID, date_placed=date_placed, bet_amount=bet_amount,
                            team1=team1, team2=team2, team_bet=team_bet, username=current_user)
                temp.save()
                #updating match odds
                #GameData_Handler.updateOdds(game_ID, team_bet, bet_amount)

    context = {
        'form':form,
        'gameData' : gameData
    }

    return render(request, 'League.html', context)


def DOTA(request):
    gameData= Games.objects.all()

    form = BetForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            user_ID = request.user.id
            game_ID = form.cleaned_data['game_ID']
            date_placed = datetime.datetime.today()
            team_bet = form.cleaned_data['team_bet']
            bet_amount = form.cleaned_data['bet_amount']
            game = Games.objects.get(match_id=game_ID)
            team1=game.team1
            team2=game.team2
            current_user = Users.objects.get(username=request.user.username)
            if (bet_amount < current_user.balance):
                current_user.balance = current_user.balance - bet_amount
                current_user.save()
                temp = Bets(user_ID=user_ID, game_ID=game_ID, date_placed=date_placed, bet_amount=bet_amount,
                            team1=team1, team2=team2, team_bet=team_bet, username=current_user)
                temp.save()
                #updating match odds
                #GameData_Handler.updateOdds(game_ID, team_bet, bet_amount)

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




def sports(request):
    return render(request, 'sports.html')


def Basketball(request):
    gameData= Games.objects.all()

    form = BetForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            user_ID = request.user.id
            game_ID = form.cleaned_data['game_ID']
            date_placed = datetime.datetime.today()
            team_bet = form.cleaned_data['team_bet']
            bet_amount = form.cleaned_data['bet_amount']
            game = Games.objects.get(match_id=game_ID)
            team1=game.team1
            team2=game.team2
            current_user = Users.objects.get(username=request.user.username)
            if (bet_amount < current_user.balance):
                current_user.balance = current_user.balance - bet_amount
                current_user.save()
                temp = Bets(user_ID=user_ID, game_ID=game_ID, date_placed=date_placed, bet_amount=bet_amount,
                            team1=team1, team2=team2, team_bet=team_bet, username=current_user)
                temp.save()

                #updating match odds
                #GameData_Handler.updateOdds(game_ID, team_bet, bet_amount)

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
            date_placed = datetime.datetime.today()
            team_bet = form.cleaned_data['team_bet']
            bet_amount = form.cleaned_data['bet_amount']
            game = Games.objects.get(match_id=game_ID)
            team1=game.team1
            team2=game.team2
            current_user = Users.objects.get(username=request.user.username)
            if (bet_amount < current_user.balance):
                current_user.balance = current_user.balance - bet_amount
                current_user.save()
                temp = Bets(user_ID=user_ID, game_ID=game_ID, date_placed=date_placed, bet_amount=bet_amount,
                            team1=team1, team2=team2, team_bet=team_bet, username=current_user)
                temp.save()

                #updating match odds
                #GameData_Handler.updateOdds(game_ID, team_bet, bet_amount)

    context = {
        'form':form,
        'gameData' : gameData
    }

    return render(request, 'Baseball.html', context)


def Hockey(request):
    gameData= Games.objects.all()

    form = BetForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            user_ID = request.user.id
            game_ID = form.cleaned_data['game_ID']
            date_placed = datetime.datetime.today()
            team_bet = form.cleaned_data['team_bet']
            bet_amount = form.cleaned_data['bet_amount']
            game = Games.objects.get(match_id=game_ID)
            team1=game.team1
            team2=game.team2
            current_user = Users.objects.get(username=request.user.username)
            if (bet_amount < current_user.balance):
                current_user.balance = current_user.balance - bet_amount
                current_user.save()
                temp = Bets(user_ID=user_ID, game_ID=game_ID, date_placed=date_placed, bet_amount=bet_amount,
                            team1=team1, team2=team2, team_bet=team_bet, username=current_user)
                temp.save()
                #updating match odds
                #GameData_Handler.updateOdds(game_ID, team_bet, bet_amount)

    context = {
        'form':form,
        'gameData' : gameData
    }

    return render(request, 'Hockey.html', context)



def test_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1') #'password1' because theres 'password1' and 'password2', one for the first box, the second for the password verification
            print(username)
            print(raw_password)
            temp=Users(username=username,password=raw_password)
            temp.save()


            return redirect('Home.html')
    else:
        print("failed")
        form = UserCreationForm()

    return render(request, 'test_signup.html', {'form': form})


def test_gamepage(request):
    gameData= Games.objects.all()

    form = BetForm(request.POST or None)
    if form.is_valid():
        user_ID = 0
        game_ID = form.cleaned_data['game_ID']
        date_placed = datetime.date.today()
        team_bet = form.cleaned_data['team_bet']
        bet_amount = form.cleaned_data['bet_amount']
        game = Games.objects.get(match_id=game_ID)
        team1=game.team1
        team2=game.team2
        temp = Bets(user_ID=user_ID, game_ID=game_ID, date_placed=date_placed, bet_amount=bet_amount, team1=team1, team2=team2, team_bet=team_bet)
        temp.save()

    context = {
        'form':form,
        'gameData' : gameData
    }

    return render(request, 'test_gamepage.html', context)


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


############################# OTHER FUNCTIONS #############################

class GameData_Handler():
    def updateOdds(matchid, team, amount):
        #If this is the first bet on a match, a row element needs to be created
        match=matchs.objects.filter(match_ID=matchid)
        if(team==match.team1):
            match.team1_amount += amount
        else:
            match.team2_amount += amount

        total = match.team1_amount + match.team2_amount

        match.team1_odds = match.team2_amount/total
        match.team2_odds = match.team1_amount/total
        match.save()

    def calculate_payout_esport(self):
        betData = Bets.objects.all()
        userData = Users.objects.all()
        link_lol = 'https://api.pandascore.co/lol/matches/past?token=fQNSOqsNLnSeovs8fk1mzbjPAsl9bYX68UBsm5hWpjIo21rk0cg'
        r_lol = requests.get(link_lol)
        data_lol = json.loads(r_lol.text)
        for game in data_lol:
            gameID = game['id']
            print("Game ID:",gameID)
            gameFinished = game['status']
            print("Finished:",gameFinished)
            if (gameFinished == 'finished'):
                winnerData = game['winner']
                winner = winnerData['name']
                print("winner:",winner)
                if(winner == None):
                    print("No winner")
                    for bet in betData :
                        if(bet.game_ID == gameID):
                            Bets.objects.filter(id=bet.id).update(winloss=0)
                else:
                    for bet in betData:
                        if(bet.game_ID == gameID):
                            if(bet.team_bet == winner):
                                if(bet.result == None):
                                    print("Correct bet")
                                    winamount = (1*bet.bet_amount) # replace 1 with the decimal odds value
                                    Bets.objects.filter(id=bet.id).update(winloss=winamount)
                                    Bets.objects.filter(id=bet.id).update(result=True)
                                    for user in userData:
                                        print("Username",user.username)
                                        print("bet user",bet.username)
                                        if(bet.username == user.username):
                                            print(user.username)
                                            newbalance = user.balance + (bet.bet_amount) + (1*bet.bet_amount) # the 1 here would be replaced by the decimal odds value
                                            print(newbalance)
                                            Users.objects.filter(username=user.username).update(balance=newbalance)
                            else:
                                if(bet.result == None):
                                    print("wrong bet")
                                    winloss = -bet.bet_amount
                                    Bets.objects.filter(game_ID=gameID).update(winloss=winloss)
                                    Bets.objects.filter(game_ID=gameID).update(result=False)
                                    # we dont need to update a loser balance because the amount the lose is already deducted when they lose

        #CSGO Payout
        link_csgo = 'https://api.pandascore.co/csgo/matches/upcoming?token=fQNSOqsNLnSeovs8fk1mzbjPAsl9bYX68UBsm5hWpjIo21rk0cg'
        r_csgo = requests.get(link_csgo)
        data_csgo = json.loads(r_csgo.text)
        for game in data_lol:
            print(game)
            gameID = game['id']
            print("Game ID:", gameID)
            gameFinished = game['status']
            print("Finished:", gameFinished)
            if (gameFinished == 'finished'):
                winnerData = game['winner']
                print("winnerData:", winnerData)
                winner = winnerData['name']
                print("winner:", winner)
                if (winner == None):
                    print("No winner")
                    for bet in betData:
                        if (bet.game_ID == gameID):
                            winloss = -bet.bet_amount
                            Bets.objects.filter(game_ID=gameID).update(winloss=winloss)
                            Bets.objects.filter(game_ID=gameID).update(result=False)
                else:
                    for bet in betData:
                        if (bet.game_ID == gameID):
                            if (bet.team_bet == winner):
                                if (bet.result == None):
                                    print("Correct bet")
                                    winamount = (1 * bet.bet_amount)  # replace 1 with the decimal odds value
                                    Bets.objects.filter(id=bet.id).update(winloss=winamount)
                                    Bets.objects.filter(id=bet.id).update(result=True)
                                    for user in userData:
                                        print("Username", user.username)
                                        print("bet user", bet.username)
                                        if (bet.username == user.username):
                                            print(user.username)
                                            newbalance = user.balance + (bet.bet_amount) + (
                                                        1 * bet.bet_amount)  # the 1 here would be replaced by the decimal odds value
                                            print(newbalance)
                                            Users.objects.filter(username=user.username).update(balance=newbalance)
                            else:
                                if (bet.result == None):
                                    print("wrong bet")
                                    winloss = -bet.bet_amount
                                    Bets.objects.filter(game_ID=gameID).update(winloss=winloss)
                                    Bets.objects.filter(game_ID=gameID).update(result=False)
                                    # we dont need to update a loser balance because the amount the lose is already deducted when they lose

        #DOTA2 Payout
        link_dota = 'https://api.pandascore.co/dota2/matches/upcoming?token=fQNSOqsNLnSeovs8fk1mzbjPAsl9bYX68UBsm5hWpjIo21rk0cg'
        r_dota = requests.get(link_dota)
        data_dota = json.loads(r_dota.text)
        for game in data_lol:
            print(game)
            gameID = game['id']
            print("Game ID:", gameID)
            gameFinished = game['status']
            print("Finished:", gameFinished)
            if (gameFinished == 'finished'):
                winnerData = game['winner']
                print("winnerData:", winnerData)
                winner = winnerData['name']
                print("winner:", winner)
                if (winner == None):
                    print("No winner")
                    for bet in betData:
                        if (bet.game_ID == gameID):
                            Bets.objects.filter(id=bet.id).update(winloss=0)
                else:
                    for bet in betData:
                        if (bet.game_ID == gameID):
                            if (bet.team_bet == winner): #IF WIN
                                if (bet.result == None):
                                    print("Correct bet")
                                    winamount = (1 * bet.bet_amount)  # replace 1 with the decimal odds value
                                    Bets.objects.filter(id=bet.id).update(winloss=winamount)
                                    Bets.objects.filter(id=bet.id).update(result=True)
                                    for user in userData:
                                        print("Username", user.username)
                                        print("bet user", bet.username)
                                        if (bet.username == user.username):
                                            print(user.username)
                                            newbalance = user.balance + (bet.bet_amount) + (
                                                        1 * bet.bet_amount)  # the 1 here would be replaced by the decimal odds value
                                            print(newbalance)
                                            Users.objects.filter(username=user.username).update(balance=newbalance)
                            else: # IF LOSE
                                if (bet.result == None):
                                    print("wrong bet")
                                    winloss = -bet.bet_amount
                                    Bets.objects.filter(game_ID=gameID).update(winloss=winloss)
                                    Bets.objects.filter(game_ID=gameID).update(result=False)
                                    # we dont need to update a loser balance because the amount the lose is already deducted when they lose

    def calculate_payout_sport(self):
        #WIP
        betData=Bets.objects.all()
        userData=Users.objects.all()
        today = datetime.date.today()
        teams = hockeyTeams(year=2021)

        #hockey
        today = datetime.date.today()
        teams = hockeyTeams(year=2021)
        Hockey_ID = "3"
        Hockey_Game_Counter =0
        for team in teams: # for every team
            print("\nTeam 1: ", team.name)
            team_1 = team.name
            teamSchedule = hockeySchedule(team.abbreviation, year=2021) # get their schedule
            for game in teamSchedule: # for every game in their schedule
                Hockey_Game_Counter += 1
                if (game.datetime.date() < today): # and if that game is in the future
                    gameID= Hockey_ID + str(Hockey_Game_Counter)
                    gameID=int(gameID)
                    print(gameID)
                    if(int(gameID) == 373):
                        print("Game ID Sport:", gameID)
                    if(game.result == 'Win'):
                        winner = team_1
                        print("winner:", winner)
                    else:
                        winner = game.opponent_name
                        print("winner:", winner)
                    if (winner == None):
                        print("No winner")
                        for bet in betData:
                            if (bet.game_ID == gameID):
                                Bets.objects.filter(id=bet.id).update(winloss=0)
                    else:
                        for bet in betData:
                            if (int(gameID) == 373):
                                print(bet.game_ID)
                            if (bet.game_ID == gameID):
                                if (bet.team_bet == winner):
                                    if (bet.result == None):
                                        print("Correct bet")
                                        winamount = (1 * bet.bet_amount)  # replace 1 with the decimal odds value
                                        Bets.objects.filter(id=bet.id).update(winloss=winamount)
                                        Bets.objects.filter(id=bet.id).update(result=True)
                                        for user in userData:
                                            print("Username", user.username)
                                            print("bet user", bet.username)
                                            if (bet.username == user.username):
                                                print(user.username)
                                                newbalance = user.balance + (bet.bet_amount) + (
                                                        1 * bet.bet_amount)  # the 1 here would be replaced by the decimal odds value
                                                print(newbalance)
                                                Users.objects.filter(username=user.username).update(balance=newbalance)
                                else:
                                    if (bet.result == None):
                                        print("wrong bet")
                                        winloss = -bet.bet_amount
                                        Bets.objects.filter(game_ID=gameID).update(winloss=winloss)
                                        Bets.objects.filter(game_ID=gameID).update(result=False)

        today = datetime.date.today()
        teams = basketballTeams(year=2021)
        Bball_ID = "2"
        Bball_Game_Counter = 0
        for team in teams:
            print("\nTeam 1: ", team.name)
            team_1 = team.name
            teamSchedule = basketballSchedule(team.abbreviation, year=2021)
            for game in teamSchedule:
                Bball_Game_Counter += 1
                if (game.datetime.date() < today):
                    gameID = Bball_ID + str(Bball_Game_Counter)
                    if (game.result == 'Win'):
                        winner = team_1
                    else:
                        winner = game.opponent_name

                    if (winner == None):
                        print("No winner")
                        for bet in betData:
                            if (bet.game_ID == gameID):
                                Bets.objects.filter(id=bet.id).update(winloss=0)
                    else:
                        for bet in betData:
                            if (bet.game_ID == gameID):
                                if (bet.team_bet == winner):
                                    if (bet.result == None):
                                        print("Correct bet")
                                        winamount = (1 * bet.bet_amount)  # replace 1 with the decimal odds value
                                        Bets.objects.filter(id=bet.id).update(winloss=winamount)
                                        Bets.objects.filter(id=bet.id).update(result=True)
                                        for user in userData:
                                            print("Username", user.username)
                                            print("bet user", bet.username)
                                            if (bet.username == user.username):
                                                print(user.username)
                                                newbalance = user.balance + (bet.bet_amount) + (
                                                        1 * bet.bet_amount)  # the 1 here would be replaced by the decimal odds value
                                                print(newbalance)
                                                Users.objects.filter(username=user.username).update(balance=newbalance)
                                else:
                                    if (bet.result == None):
                                        print("wrong bet")
                                        winloss = -bet.bet_amount
                                        Bets.objects.filter(game_ID=gameID).update(winloss=winloss)
                                        Bets.objects.filter(game_ID=gameID).update(result=False)

        today = datetime.date.today()
        teams = baseballTeams(year=2021)
        Baseball_ID = "1"
        Baseball_Game_Counter = 0
        for team in teams:
            print("\nTeam 1: ", team.name)
            team_1 = team.name
            teamSchedule = baseballSchedule(team.abbreviation, year=2021)
            for game in teamSchedule:
                Baseball_Game_Counter += 1
                if (today > game.datetime.date()):
                    gameID = Baseball_ID + str(Baseball_Game_Counter)
                    if (game.result == 'Win'):
                        winner = team_1
                    else:
                        winner = game.opponent_abbr

                    if (winner == None):
                        print("No winner")
                        for bet in betData:
                            if (bet.game_ID == gameID):
                                Bets.objects.filter(id=bet.id).update(winloss=0)
                    else:
                        for bet in betData:
                            if (bet.game_ID == gameID):
                                if (bet.team_bet == winner):
                                    if (bet.result == None):
                                        print("Correct bet")
                                        winamount = (1 * bet.bet_amount)  # replace 1 with the decimal odds value
                                        Bets.objects.filter(id=bet.id).update(winloss=winamount)
                                        Bets.objects.filter(id=bet.id).update(result=True)
                                        for user in userData:
                                            print("Username", user.username)
                                            print("bet user", bet.username)
                                            if (bet.username == user.username):
                                                print(user.username)
                                                newbalance = user.balance + (bet.bet_amount) + (
                                                        1 * bet.bet_amount)  # the 1 here would be replaced by the decimal odds value
                                                print(newbalance)
                                                Users.objects.filter(username=user.username).update(balance=newbalance)
                                else:
                                    if (bet.result == None):
                                        print("wrong bet")
                                        winloss = -bet.bet_amount
                                        Bets.objects.filter(game_ID=gameID).update(winloss=winloss)
                                        Bets.objects.filter(game_ID=gameID).update(result=False)


    def get_api_data(self):
        print("Getting API DATA")
        # Clear games data table
        Games.objects.all().delete()


        # Hockey
        today = datetime.date.today()
        teams = hockeyTeams(year=2021)
        Hockey_ID = "3"
        Hockey_Game_Counter =0
        Game_data = Games(name="Vegas Golden Knights Anaheim Ducks", time_data=datetime.datetime.strptime('2021-02-27',"%Y-%m-%d"), sport='Hockey', team1="Vegas Golden Knights", team1_amount=0,
                          team1_odds=.5, team2="Anaheim Ducks", team2_amount=0, team2_odds=.5, match_id="373")
        Game_data.save()
        for team in teams: # for every team
            print("\nTeam 1: ", team.name)
            team_1 = team.name
            teamSchedule = hockeySchedule(team.abbreviation, year=2021) # get their schedule
            for game in teamSchedule: # for every game in their schedule
                Hockey_Game_Counter += 1
                if (game.datetime.date() > today): # and if that game is in the future
                    add_to_list = True # flag it so it will be added to the database
                    startTime = game.datetime # set the time
                    print(game.datetime)
                    team_2 = game.opponent_name # get their opponent from the API
                    gameName = team_1 + " " + team_2 + " " + str(game.datetime.date()) # append the two teams and game date
                    # check for duplicate matches
                    for each in Games.objects.all(): # for each game in the database
                        if (each.team1 == team_2 and each.team2 == team_1 and each.time_data == startTime): # if that game as the same 2 teams and startTime
                            add_to_list = False #we conclude its in the database, and set the flag for it to be added to false
                    #now we add all new games to the database
                    if (add_to_list != False):
                        print("\nTeam 2: ", team.name)
                        print("\nStarting time", startTime)
                        Game_data = Games()
                        Game_ID = Hockey_ID + str(Hockey_Game_Counter)
                        Game_data = Games(name=gameName, time_data=startTime, sport='Hockey', team1=team_1, team1_amount=0, team1_odds=.5, team2=team_2, team2_amount=0, team2_odds=.5, match_id=Game_ID)
                        Game_data.save()
                        print("\ndata added")
                    add_to_list = True
        # Basketball
        today = datetime.date.today()
        teams = basketballTeams(year=2021)
        Bball_ID = "2"
        Bball_Game_Counter = 0
        for team in teams:
            print("\nTeam 1: ", team.name)
            team_1 = team.name
            teamSchedule = basketballSchedule(team.abbreviation, year=2021)
            for game in teamSchedule:
                Bball_Game_Counter += 1
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
                        Game_ID = Bball_ID + str(Bball_Game_Counter)
                        Game_data = Games(name=gameName, time_data=startTime, sport='BasketBall', team1=team_1, team1_amount=0, team1_odds=.5, team2=team_2, team2_amount=0, team2_odds=.5, match_id=Game_ID)
                        Game_data.save()
                        print("\ndata added")
                    add_to_list = True

        # Baseball
        today = datetime.date.today()
        month = timedelta(days=+30)
        monthlater = today+month

        teams = baseballTeams(year=2021)
        Baseball_ID = "1"
        Baseball_Game_Counter = 0
        for team in teams:
            print("\nTeam 1: ", team.name)
            team_1 = team.name
            teamSchedule = baseballSchedule(team.abbreviation, year=2021)
            for game in teamSchedule:
                Baseball_Game_Counter += 1
                if (today<game.datetime.date() and game.datetime.date()<monthlater):
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
                        Game_ID = Baseball_ID + str(Baseball_Game_Counter)
                        Game_data = Games(name=gameName, time_data=startTime, sport='baseball', team1=team_1, team1_amount=0, team1_odds=.5, team2=team_2, team2_amount=0, team2_odds=.5, match_id=Game_ID)
                        Game_data.save()
                        print("\ndata added")
                    add_to_list = True


        # League of Legends | LOL
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
                Game_data = Games(name=gameName, time_data=time, sport='LOL', team1=team_1, team1_amount=0, team1_odds=.5, team2=team_2, team2_amount=0, team2_odds=.5, match_id=gameID)
                Game_data.save()
            print("\n")

        print("\nDONE WITH LOL")
        # DOTA 2
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
                Game_data = Games(name=gameName, time_data=time, sport='dota2', team1=team_1, team1_amount=0, team1_odds=.5, team2=team_2, team2_amount=0, team2_odds=.5, match_id=gameID)
                Game_data.save()
            print("\n")

        print("\nDONE WITH DOTA2")

        # CSGO
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
                Game_data = Games(name=gameName, time_data=time, sport='CSGO', team1=team_1, team1_amount=0, team1_odds=.5, team2=team_2, team2_amount=0, team2_odds=.5, match_id=gameID)
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
