import Teams
import csv
import datetime as dt
import matplotlib.pyplot as plt
from collections import OrderedDict
from constants import _Const

CONST = _Const()
input_date = input("Date (dd/mm/yy format): ")
stop_date = dt.datetime.strptime(input_date, '%d/%m/%y')

data = Teams.csvopen(CONST.INPUT_FILE)
next(data)

teams = {}
points = 0
played = 0
sg = 0
ag = 0
goal_diff = 0

for row in data:
    date=dt.datetime.strptime(row[1], '%d/%m/%y')
    if date>stop_date:
        break
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

    if home_team not in teams:
        teams[home_team] = Teams.Team(name = home_team)
    if away_team not in teams:
        teams[away_team] = Teams.Team(name = away_team)
    teams[home_team].update(home_goals, away_goals, home_shots, home_sht, home_corners)
    teams[away_team].update(away_goals, home_goals, away_shots, away_sht, away_corners)

sorted_teams = sorted(teams.values(), reverse=True, key=lambda t: t.points)

output = open(CONST.OUTPUT_PATH + 'Standings.txt','w')
output.write('Date Table: ' + input_date + '\n')

for team in sorted_teams:
    output.write(str(team) + '\n')

output.close()
