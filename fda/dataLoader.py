import Teams
import csv
import datetime as dt
import numpy as np
from constants import _Const

def LoadTeamData(stop_date, input_team):    
    CONST = _Const()
    data = Teams.csvopen(CONST.INPUT_FILE)
    next(data)

    fixtures = {}

    for row in data:
        date=dt.datetime.strptime(row[1], '%d/%m/%y')
        if date>stop_date:
            break
        fixture_date = dt.datetime.strptime(row[1], '%d/%m/%y').date()
        home_team = row[2]
        away_team = row[3]
        home_goals = int(row[4])
        away_goals = int(row[5])
        home_shots = int(row[11])
        away_shots = int(row[12])
        home_sht = int(row[13])
        away_sht = int(row[14])
        home_corners = int(row[17])
        away_corners = int(row[18])
        if row[6] == 'H' : winner = 2
        elif row[6] == 'A' : winner = -1
        elif row[6] == 'D' : winner = 1

        if (home_team == input_team or away_team == input_team):
            id_value = home_team + '_' + away_team

            if id_value not in fixtures:
                fixtures[id_value] = Teams.Fixture(name = id_value, fixture_date = fixture_date, winner=winner)

            fixtures[id_value].hometeam = Teams.Team(name = home_team)
            fixtures[id_value].awayteam = Teams.Team(name = away_team)

            fixtures[id_value].hometeam.update(home_goals, away_goals, home_shots, home_sht, home_corners)
            fixtures[id_value].awayteam.update(away_goals, home_goals, away_shots, away_sht, away_corners)

    return fixtures

def LoadAllData(stop_date):    
    CONST = _Const()
    data = Teams.csvopen(CONST.INPUT_FILE)
    next(data)

    fixtures = {}

    for row in data:
        date=dt.datetime.strptime(row[1], '%d/%m/%y')
        if date>stop_date:
            break
        fixture_date = dt.datetime.strptime(row[1], '%d/%m/%y').date()
        home_team = row[2]
        away_team = row[3]
        home_goals = int(row[4])
        away_goals = int(row[5])
        home_shots = int(row[11])
        away_shots = int(row[12])
        home_sht = int(row[13])
        away_sht = int(row[14])
        home_corners = int(row[17])
        away_corners = int(row[18])
        if row[6] == 'H' : winner = 2
        elif row[6] == 'A' : winner = -1
        elif row[6] == 'D' : winner = 1

        id_value = home_team + '_' + away_team

        if id_value not in fixtures:
            fixtures[id_value] = Teams.Fixture(name = id_value, fixture_date = fixture_date, winner=winner)

        fixtures[id_value].hometeam = Teams.Team(name = home_team)
        fixtures[id_value].awayteam = Teams.Team(name = away_team)

        fixtures[id_value].hometeam.update(home_goals, away_goals, home_shots, home_sht, home_corners)
        fixtures[id_value].awayteam.update(away_goals, home_goals, away_shots, away_sht, away_corners)

    return fixtures

def GetAllTeamsWithTotals(stop_date):
    fixtures = LoadAllData(stop_date)

    teams = {}

    for fixture in fixtures:
        
        fix = fixtures.get(fixture)

        home_team = fix.hometeam.name
        away_team = fix.awayteam.name

        if home_team not in teams:
            teams[home_team] = Teams.Team(name = home_team)
        if away_team not in teams:
            teams[away_team] = Teams.Team(name = away_team)
        teams[home_team].update(fix.hometeam.goals_scored, fix.hometeam.goals_allowed, fix.hometeam.shots[0], fix.hometeam.shots_on_target[0], fix.hometeam.corners[0])
        teams[away_team].update(fix.awayteam.goals_scored, fix.awayteam.goals_allowed, fix.awayteam.shots[0], fix.awayteam.shots_on_target[0], fix.awayteam.corners[0])

    return teams
