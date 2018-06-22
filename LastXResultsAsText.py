import Teams
import csv
import datetime as dt
import matplotlib.pyplot as plt
from collections import OrderedDict
import numpy as np

input_date = input("Date (dd/mm/yy format): ")
stop_date = dt.datetime.strptime(input_date, '%d/%m/%y')

input_team = input("Team: ")

data = Teams.csvopen('inputs/E0.csv')
next(data)

fixtures = {}
points = 0
played = 0
sg = 0
ag = 0
goal_diff = 0

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

    if (home_team == input_team):
        id_value = home_team + '_' + away_team

        if id_value not in fixtures:
            fixtures[id_value] = Teams.Fixture(name = id_value, fixture_date = fixture_date, winner=winner)

        fixtures[id_value].hometeam = Teams.Team(name = home_team)
        fixtures[id_value].awayteam = Teams.Team(name = away_team)

        fixtures[id_value].hometeam.update(home_goals, away_goals, home_shots, home_sht, home_corners)
        fixtures[id_value].awayteam.update(away_goals, home_goals, away_shots, away_sht, away_corners)

sorted_teams = sorted(fixtures.values(), reverse=False, key=lambda t: t.fixture_date)
last_10_items = sorted_teams[-10:]

output = open('outputs/' + input_team +'_lastX.txt','w')
output.write('Date Table: ' + input_date + '\n')

for team in last_10_items:
    output.write(str(team.hometeam) + ' ' + str(team.hometeam.goals_scored) + ' vs ' + str(team.awayteam.goals_scored) + ' ' + str(team.awayteam) + ' ' + str(team.fixture_date) + '\n') #str(team) + 

output.close()