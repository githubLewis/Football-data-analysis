import csv
import Teams
import collections
import numpy as np
from scipy.misc import factorial


def csvopen(filename):
    csv_file = open(filename)
    data = csv.reader(csv_file, delimiter=',')
    return data

def mov_avg(data,window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(data, window, 'valid')

def poisson(k, lam):
    return ((lam**k)/factorial(k))* np.exp(-lam)

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
        self.goals = []
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
    def scored(self, scored):
        self.goals.append(scored)

class Fixture:
    def __init__(self, name, fixture_date, winner):
        self.name = name
        self.hometeam = Team
        self.awayteam = Team
        self.fixture_date = fixture_date
        self.winner = winner
    def __repr__(self):
        return str((self.name, self.hometeam, self.awayteam, self.fixture_date, self.winner))
