import matplotlib.pyplot as plt
import csv
from collections import defaultdict


def get_data():
    file = open("matches.csv")
    delivery = csv.DictReader(file)
    return delivery

def get_runs(delivery):
    runs = {}
    runs["2016"] = {}
    for match in delivery:
        year = match["season"]
        if str(year) == "2016":
            runs[year][match["winner"]] = runs[year].get(match["winner"],0) + int(match["win_by_runs"])
    extra_runs= runs["2016"]
    for i in extra_runs:
        print(i," : ",extra_runs[i])
    return extra_runs

def plot_graph(batting_teams,extra_score):
    plt.bar(batting_teams, extra_score)
    plt.xlabel('Team')
    plt.ylabel('Runs Conceded')
    plt.title('Run Conceded by each Team')
    plt.xticks(rotation=25, ha='right')
    for i, score in enumerate(extra_score):
        plt.text(i, score, str(score), ha='center', va='bottom')
    plt.show()

delivery = get_data()
extra_runs = get_runs(delivery)
batting_teams = list(extra_runs.keys())
extra_score = list(extra_runs.values())

plot_graph(batting_teams,extra_score)