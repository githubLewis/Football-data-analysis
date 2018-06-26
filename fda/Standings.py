import Teams
import csv
import datetime as dt
import matplotlib.pyplot as plt
from collections import OrderedDict
from constants import _Const
import dataLoader

CONST = _Const()
input_date = input("Date (dd/mm/yy format): ")
stop_date = dt.datetime.strptime(input_date, '%d/%m/%y')

teams = dataLoader.GetAllTeamsWithTotals(stop_date)

sorted_teams = sorted(teams.values(), reverse=True, key=lambda t: t.points)

output = open(CONST.OUTPUT_PATH + 'Standings.txt','w')
output.write('Date Table: ' + input_date + '\n')

for team in sorted_teams:
    output.write(str(team) + '\n')

output.close()
