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
output = open(CONST.OUTPUT_PATH + input_team +'_lastX.html','w')
output.write('<html><body>')
output.write('<p>Date Table: ' + input_date + '</p>')

output.write('<h2>Last 10 results</h2>')
output.write('<table>')
for team in last_10_items:
    output.write('<tr><td>{}</td><td>{}</td><td>{}</td><td>vs<td>{}</td><td>{}</td></tr>'.format(
        team.fixture_date,
        team.hometeam.name,
        team.hometeam.goals_scored,
        team.awayteam.goals_scored,
        team.awayteam.name
    ))

output.write('</table>')
output.write('</body></html>')
output.close()