import Teams
import csv
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

input_date = input("Date (dd/mm/yy format): ")
input_team = input("Team: ")
avg_window = input("Window size for rolling average: ")
stop_date = dt.datetime.strptime(input_date, '%d/%m/%y')

data = Teams.csvopen('inputs/E0.csv')
next(data)
#input_team = raw_input("Team: ")

def mov_avg(data,window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(data, window, 'valid')

teams = {}
points = 0
played = 0
sg = 0 #dati golovi
ag = 0 #primljeni golovi
goal_diff = 0 #gol razlika

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

output = open('outputs/Standings.txt','w')
output.write('Date Table: ' + input_date + '\n')
for team in sorted_teams:
    output.write(str(team) + '\n')
output.close()

avg_shots = teams.get(input_team, None).shots
avg_sht = teams.get(input_team, None).shots_on_target
avg_corners = teams.get(input_team, None).corners
shots_mov_avg = mov_avg(avg_shots, avg_window)
sht_mov_avg = mov_avg(avg_sht, avg_window)
corners_mov_avg = mov_avg(avg_corners, avg_window)
plt.plot(shots_mov_avg, label = "Shots on goal")
plt.plot(sht_mov_avg, label = "Shots on target")
plt.plot(corners_mov_avg, label = "Corners")
plt.axis([0, 35, 0, 25])
plt.title("Rolling average")
plt.xlabel("Number of matches")
plt.ylabel("Average value")
plt.legend()
plt.savefig('outputs/tabela.jpg')
plt.clf()
                                                             