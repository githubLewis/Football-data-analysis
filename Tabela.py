import csv
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

input_date = raw_input("Datum (dd/mm/yy format): ")
input_team = raw_input("Tim: ")
avg_window = raw_input("Velicina prozora za rolling average: ")
stop_date = dt.datetime.strptime(input_date, '%d/%m/%y')
csv_file = open('E0.csv', 'rb')
data = csv.reader(csv_file, delimiter=',')
next(data)

class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.played = 0
        self.goals_scored = 0
        self.goals_allowed = 0
        self.goal_diff = 0
        self.shots = []
        self.shots_on_target = []
        self.corners = []
    def __repr__(self):
        return str((self.name, self.points, self.played, self.goals_scored, self.goals_allowed, self.goal_diff))
    def update(self, scored, allowed, sh, sht, cor):
        self.played+=1
        if scored == allowed:
            self.points+=1
        elif scored> allowed:
            self.points+=3
        self.goals_scored += scored
        self.goals_allowed += allowed
        self.goal_diff += scored - allowed
        self.shots.append(sh)
        self.shots_on_target.append(sht)
        self.corners.append(cor)
       

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
        teams[home_team] = Team(name = home_team)
    if away_team not in teams:
        teams[away_team] = Team(name = away_team)
    teams[home_team].update(home_goals, away_goals, home_shots, home_sht, home_corners)
    teams[away_team].update(away_goals, home_goals, away_shots, away_sht, away_corners)

sorted_teams = sorted(teams.values(), reverse=True, key=lambda t: t.points)

output = open('Standings.txt','w')
output.write('Tabela za datum: ' + input_date + '\n')
for team in sorted_teams:
    output.write(str(team) + '\n')
output.close()

avg_shots = teams.get(input_team, None).shots
avg_sht = teams.get(input_team, None).shots_on_target
avg_corners = teams.get(input_team, None).corners
shots_mov_avg = mov_avg(avg_shots, avg_window)
sht_mov_avg = mov_avg(avg_sht, avg_window)
corners_mov_avg = mov_avg(avg_corners, avg_window)
plt.plot(shots_mov_avg, label = "Sutevi na gol")
plt.plot(sht_mov_avg, label = "Sutevi u okvir gola")
plt.plot(corners_mov_avg, label = "Korneri")
plt.axis([0, 35, 0, 25])
plt.title("Rolling average grafik")
plt.xlabel("Broj utakmice")
plt.ylabel("Prosecna vrednost")
plt.legend()
plt.show()
                                                             