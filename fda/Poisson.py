import Teams
import collections
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from constants import _Const
import dataLoader

CONST = _Const()
teams = {}

fixtures = dataLoader.LoadAllData(dt.datetime.now())
output = open(CONST.OUTPUT_PATH + 'Parameters.txt','w')

for fixture in fixtures:
    
    fix = fixtures.get(fixture)
    
    home_team = fix.hometeam.name
    away_team = fix.awayteam.name
    home_goals = fix.hometeam.goals_scored
    away_goals = fix.awayteam.goals_scored

    if home_team not in teams:
        teams[home_team] = Teams.Team(name = home_team)
    if away_team not in teams:
        teams[away_team] = Teams.Team(name = away_team)
    teams[home_team].scored(home_goals)
    teams[away_team].scored(away_goals)

for team in teams.keys():
    input_team = team
    goal_list = []
    prob = []
    prob_err = []
    goal_no = []
    no_of_goals = []
    i = 0
    goal_list = teams.get(input_team).goals
    goal_list.sort()
    counted = collections.Counter(goal_list)
    no_of_occurencies = list(counted.values())
    no_of_goals = list(counted.keys())
    for item in no_of_goals:
        goal_no.append(no_of_goals[i])
        probability = float(no_of_occurencies[i])/len(goal_list)
        probability_err =  probability/np.sqrt(no_of_occurencies[i])
        prob.append(probability)
        prob_err.append(probability_err)
        i += 1


    parameters, cov = curve_fit(Teams.poisson, no_of_goals, no_of_occurencies)
    x_data = np.linspace(0, 8, 1000)

    #if parameters[0] < 0:
        #parameters[0] = 1
    output.write(input_team + str(parameters) + '\n')
    plt.plot(goal_no, prob, '*', label = 'Data points')
    plt.plot(x_data, Teams.poisson(x_data, *parameters), 'r-', lw=3, label = 'Poisson fit')
    plt.errorbar(goal_no, prob, yerr = prob_err, fmt='', linestyle = 'none')
    plt.title('Probability distribution of number of goals in a match for ' + input_team)
    plt.xlabel('Number of goals')
    plt.ylabel('Probability')
    plt.xlim(-1, (max(no_of_goals)+1))
    plt.legend()
    plt.savefig(CONST.OUTPUT_PATH + input_team + '_psn.jpg')
    plt.clf()
    
output.close()