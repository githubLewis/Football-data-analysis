import Teams
import csv
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
from constants import _Const
import dataLoader

CONST = _Const()

# Inputs
input_date = input("Date (dd/mm/yy format): ")
avg_window_sz = input("Window size for rolling average: ")
stop_date = dt.datetime.strptime(input_date, '%d/%m/%y')

avg_window = int(avg_window_sz)

# Load the data
teams = dataLoader.GetAllTeamsWithTotals(stop_date)

# Calculate and build the graph
for team in teams.keys():
    print(team)
    input_team = team
    avg_shots = teams.get(input_team, None).shots
    avg_sht = teams.get(input_team, None).shots_on_target
    avg_corners = teams.get(input_team, None).corners
    shots_mov_avg = Teams.mov_avg(avg_shots, avg_window)
    sht_mov_avg = Teams.mov_avg(avg_sht, avg_window)
    corners_mov_avg = Teams.mov_avg(avg_corners, avg_window)
    plt.plot(shots_mov_avg, label = "Shots on goal")
    plt.plot(sht_mov_avg, label = "Shots on target")
    plt.plot(corners_mov_avg, label = "Corners")
    plt.axis([0, 35, 0, 25])
    plt.title("Rolling average")
    plt.xlabel("Number of matches")
    plt.ylabel("Average value")
    plt.legend()
    plt.savefig(CONST.OUTPUT_PATH + team + '_avg.jpg')
    plt.clf()
