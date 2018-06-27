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

output = open(CONST.OUTPUT_PATH + 'leaguetable.html','w')
output.write('<table>')
output.write('<thead>')
output.write('<tr>')
output.write('<th></th>')
output.write('<th></th>')
output.write('<th></th>')
output.write('<th></th>')
output.write('<th></th>')
output.write('<th></th>')
output.write('</tr>')
output.write('</thead>')
output.write('<tbody>')

for team in sorted_teams:
    output.write('<tr>')
       
    output.write('<td>')
    output.write('<a href="team/' + str(team.name) + '">' + str(team.name) + '</a>')
    output.write('</td>')
    
    output.write('<td>')
    output.write(str(team.points))
    output.write('</td>')

    output.write('<td>')
    output.write(str(team.played))
    output.write('</td>')

    output.write('<td>')
    output.write(str(team.goals_scored))
    output.write('</td>')

    output.write('<td>')
    output.write(str(team.goals_allowed))
    output.write('</td>')

    output.write('<td>')
    output.write(str(team.goal_diff))
    output.write('</td>')

    output.write('</tr>')

output.write('</tbody>')
output.write('<tfoot>')
output.write('<tr>')
output.write('<td></td>')
output.write('<td></td>')
output.write('<td></td>')
output.write('<td></td>')
output.write('<td></td>')
output.write('<td></td>')
output.write('</tr>')
output.write('</tfoot>')
output.write('</table>')
output.close()
