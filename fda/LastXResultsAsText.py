import Teams
import csv
import datetime as dt
import matplotlib.pyplot as plt
from collections import OrderedDict
import numpy as np
from constants import _Const
import dataLoader

CONST = _Const()

# Inputs
input_team = input("Team: ")
input_date = input("Date (dd/mm/yy format): ")
stop_date = dt.datetime.strptime(input_date, '%d/%m/%y')

# Load the data
fixtures = dataLoader.LoadTeamData(dt.datetime.now(), input_team)

# Sort it
sorted_teams = sorted(fixtures.values(), reverse=False, key=lambda t: t.fixture_date)
last_10_items = sorted_teams[-10:]

# Build the text file
output = open(CONST.OUTPUT_PATH + input_team +'_lastX.txt','w')
output.write('Date Table: ' + input_date + '\n')

for team in last_10_items:
    output.write(str(team.hometeam) + ' ' + str(team.hometeam.goals_scored) + ' vs ' + str(team.awayteam.goals_scored) + ' ' + str(team.awayteam) + ' ' + str(team.fixture_date) + '\n') #str(team) + 

output.close()