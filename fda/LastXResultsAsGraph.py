import Teams
import csv
import datetime as dt
import matplotlib.pyplot as plt
from collections import OrderedDict
import numpy as np
from constants import _Const

CONST = _Const()
input_date = input("Date (dd/mm/yy format): ")
stop_date = dt.datetime.strptime(input_date, '%d/%m/%y')

input_team = input("Team: ")

data = Teams.csvopen(CONST.INPUT_FILE)
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

colors = []
dates=[]

y = np.asarray([o.winner for o in last_10_items] )
dates = np.asarray([o.fixture_date for o in last_10_items])
idx = np.asarray([i for i in range(len(dates))])

# sort the colours out
for h in last_10_items:
    if h.winner == 2:
        colors.append('g')
    elif h.winner == 1:
        colors.append('b')
    else:
        colors.append('r')
    
fig, ax = plt.subplots(figsize = (10,4))

plt.tick_params(
    axis='y',          # changes apply to the y-axis
    which='both',      # both major and minor ticks are affected
    left='off',  
    top='off', 
    right='off', 
    bottom='off',
    labelleft='off', 
    labeltop='off', 
    labelright='off', 
    labelbottom='off'
    )

width = 1

ax.bar(idx, y, width=width, color=colors )
ax.set_xticks(idx)
ax.set_xticklabels(dates, rotation=65)
ax.set_xlabel('Fixture date')
ax.set_ylabel('Result')
fig.tight_layout()

plt.savefig(CONST.OUTPUT_PATH + input_team + '_last10_bar.jpg')