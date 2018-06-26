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

# Build the graph
colors = []
dates=[]

y = np.asarray([o.winner for o in last_10_items] )
dates = np.asarray([o.fixture_date for o in last_10_items])
idx = np.asarray([i for i in range(len(dates))])

# Sort the colours out
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