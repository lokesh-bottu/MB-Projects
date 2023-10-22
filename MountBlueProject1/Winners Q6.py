import matplotlib.pyplot as plt
import csv
from collections import defaultdict



def get_data(path):
    file = open(path)
    delivery = csv.DictReader(file)
    return delivery

def get_teams(delivery): 
    teams = {}
    for match in delivery:
        year = match["season"]
        winner = match["winner"]
        
        if year not in teams:
            teams[year] = {}

        if winner in teams[year]:
            teams[year][winner] += 1
        else:
            teams[year][winner] = 1
    for i in teams:
        print(i," : ",teams[i])

    return teams



def plot_graph(teams):
    years = list(teams.keys())
    group = list(teams[years[0]].keys())

    fig, ax = plt.subplots(figsize=(12, 6))

    bottom = [0] * len(years)

    for te in group:
        team_values = [teams[year].get(te, 0) for year in years]
        ax.bar(years, team_values, label=te, bottom=bottom)
        bottom = [bottom[i] + team_values[i] for i in range(len(years))]

    ax.set_xlabel('Team')
    ax.set_ylabel('Number of Matches')
    ax.set_title('Indian Premier League (IPL) Matches Played by Team (2017-2008)')

    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.tight_layout()
    plt.show()

data = get_data("matches.csv")
teams = get_teams(data)
plot_graph(teams)