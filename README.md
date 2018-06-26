# Football-data-analysis
Using Python tools to analyze football statistics

## Overview
Collection of scripts used to generate analysis of football statistics.

### poisson.py
Generates a poisson graph jpg for each team in the file.

![Southampton Poisson](/outputs/examples/Southampton_psn.jpg?raw=true)

### standings.py
Generates a league table.

### averages.py
Generates a rolling average graph (shots on goal, shots on target, corners) for each team in the file.

![Southampton Averages](/outputs/examples/Southampton_avg.jpg?raw=true)

### LastXResultsAsGraph.py
Generates a bar graph displaying the last 10 results in a graphical fashion.

![Southampton Last10](/outputs/examples/Southampton_last10_bar.jpg?raw=true)

### LastXResultsAsText.py
Generates a text file displaying the last 10 results in text format.

### Teams.py
Shared code, contains the team, fixture classes and helper functions, such as poisson & csvopen.

### dataLoader.py
Used to load the data from the CSV.

### constants.py
Holds constant values used across scripts (paths etc)

## Usage
Scripts can be run in the Python terminal.

## Build notes
N/A

## Additional comments

Data source is a CSV file downloaded from: [http://www.football-data.co.uk](http://www.football-data.co.uk)
