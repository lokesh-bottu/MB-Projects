import matplotlib.pyplot as plt
import csv
from collections import defaultdict

def get_data():
    file = open("Deliveries.csv")
    delivery = csv.DictReader(file)
    return delivery


#search for each team if there are runs already scored then add the current runs to it 
#otherwise the scored runs will be 0
#so the get function return 0 in case it is not found in the dictionary.
def get_score(delivery):
    teams = {}
    for ball in delivery:
        teams[ball["batting_team"]] = int(teams.get(ball["batting_team"],0)) + int(ball["total_runs"])
    return teams
    
def plot_graph(batting_teams,score):
    plt.bar(batting_teams,score)
    plt.xlabel('Team')
    plt.ylabel('Runs Scored')
    plt.title("Runs Scored  by each Team")
    plt.xticks(rotation=270)
    for i, score in enumerate(score):
        plt.text(i, score, str(score), ha='center', va='bottom')
    plt.show()


delivery = get_data()
teams = get_score(delivery)

for i in teams:
    print(i," : ",teams[i])

batting_teams = list(teams.keys())
score = list(teams.values())
plot_graph(batting_teams,score)