from sportsipy.mlb.schedule import Schedule as baseballSchedule
from sportsipy.mlb.teams import Teams as baseballTeams
from sportsipy.fb.schedule import Schedule as soccerSchedule
from sportsipy.fb.team import Team as soccerTeams
from sportsipy.nba.schedule import Schedule as basketballSchedule
from sportsipy.nba.teams import Teams as basketballTeams
from sportsipy.nfl.schedule import Schedule as footballSchedule
from sportsipy.nfl.teams import Teams as footballTeams
from datetime import *


def getBaseballSchedule():
    todaysGames = []
    today = date.today()
    teams = baseballTeams(2021)
    for team in teams:
        print(team.abbreviation)
        teamSchedule = baseballSchedule(team.abbreviation)
        for game in teamSchedule:
            if game.datetime.date() == today:
                todaysGames.append(game)
                print("Team added to list")
    return todaysGames


def getBasketballSchedule():
    todaysGames = []
    today = date.today()
    teams = basketballTeams(2021)
    for team in teams:
        print(team.abbreviation)
        teamSchedule = basketballSchedule(team.abbreviation)
        for game in teamSchedule:
            if game.datetime.date() == today:
                todaysGames.append(game)
                print("Team added to list")
    return todaysGames


def getFootballSchedule():
    todaysGames = []
    today = date.today()
    teams = footballTeams(2021)
    for team in teams:
        print(team.abbreviation)
        teamSchedule = footballSchedule(team.abbreviation)
        for game in teamSchedule:
            if game.datetime.date() == today:
                todaysGames.append(game)
                print("Team added to list")
    return todaysGames


if __name__ == "__main__":
    #football_schedule = getFootballSchedule()
    #basketball_schedule = getBasketballSchedule()
    baseball_schedule = getBaseballSchedule()
