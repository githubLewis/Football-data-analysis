import Teams
import collections
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
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

goalsfor = 0
goalsagainst = 0
cornersfor = 0
cornersagainst = 0
btts = 0
oOF = 0
oTF = 0
cleanSheet = 0
failedToScore = 0

for fixture in last_10_items:
    if (fixture.hometeam.name == input_team):
        goalsfor += fixture.hometeam.goals_scored
        goalsagainst += fixture.awayteam.goals_scored
        cornersagainst += fixture.awayteam.corners[0]
        cornersfor += fixture.hometeam.corners[0]
    elif (fixture.awayteam.name == input_team):
        goalsfor += fixture.awayteam.goals_scored
        goalsagainst += fixture.hometeam.goals_scored
        cornersagainst += fixture.hometeam.corners[0]
        cornersfor += fixture.awayteam.corners[0]

    if (fixture.hometeam.name == input_team and fixture.hometeam.goals_scored == 0 ):
        failedToScore += 1
    elif (fixture.awayteam.name == input_team and fixture.awayteam.goals_scored == 0 ):
        failedToScore += 1

    if (fixture.hometeam.name == input_team and fixture.awayteam.goals_scored == 0 ):
        cleanSheet += 1
    elif (fixture.awayteam.name == input_team and fixture.hometeam.goals_scored == 0 ):
        cleanSheet += 1

    if ((fixture.hometeam.goals_scored > 0) and (fixture.awayteam.goals_scored > 0)):
        btts +=1

    if ((fixture.hometeam.goals_scored + fixture.awayteam.goals_scored) > 2.5):
        oTF +=1
    elif ((fixture.hometeam.goals_scored + fixture.awayteam.goals_scored) > 1.5):
        oOF +=1

# Build the text file
output = open(CONST.OUTPUT_PATH + input_team +'_statcard.html','w')
output.write('<html><body>')
output.write('<p>Date Table: ' + input_date + '</p>')

avgGoalsFor = goalsfor / 10
avgGoalsAgainst = goalsagainst / 10
avgTotalGoals = avgGoalsFor + avgGoalsAgainst

avgCornersAgainst = cornersagainst / 10
avgCornersFor = cornersfor / 10
avgTotalCorners = avgCornersFor + avgCornersAgainst

output.write('<h2>Corners</h2>')
output.write('<table>')
output.write('<tr><td>Avg. Corners For</td><td>' + '{:.2f}'.format(avgCornersFor) + '</td></tr>')
output.write('<tr><td>Avg. Corners Against</td><td>' + '{:.2f}'.format(avgCornersAgainst) + '</td></tr>')
output.write('<tr><td>Total Corners</td><td>' + '{:.2f}'.format(avgTotalCorners)  + '</td></tr>')
output.write('</table>')

output.write('<h2>Goals For/Against</h2>')
output.write('<table>')
output.write('<tr><td>Avg. Goals For</td><td>' + '{:.2f}'.format(avgGoalsFor)  + '</td></tr>')
output.write('<tr><td>Avg. Goals Against</td><td>' + '{:.2f}'.format(avgGoalsAgainst)  + '</td></tr>')
output.write('<tr><td>Total Goals</td><td>' + '{:.2f}'.format(avgTotalGoals)  + '</td></tr>')
output.write('</table>')

output.write('<h2>Other</h2>')
output.write('<table>')
output.write('<tr><td>Number of game btts</td><td>' + '{:.2f}'.format(btts)  + '</td></tr>')
output.write('<tr><td>Number of clean sheets</td><td>' + '{:.2f}'.format(cleanSheet)  + '</td></tr>')
output.write('<tr><td>Number of game failed to score</td><td>' + '{:.2f}'.format(failedToScore)  + '</td></tr>')
output.write('<tr><td>Number of game with Over 1.5 Goals</td><td>' + '{:.2f}'.format(oOF)  + '</td></tr>')
output.write('<tr><td>Number of game with Over 2.5 Goals</td><td>' + '{:.2f}'.format(oTF)  + '</td></tr>')
output.write('</table>')


output.write('</body></html>')

output.close()
