import csv
from collections import defaultdict
import matplotlib.pyplot as plt



def get_top10(sorted_economy_rates):
    cnt = 1
    top10 = {}
    for i in sorted_economy_rates:
        top10[i ] = sorted_economy_rates[i]
        if cnt == 10:
            break
        else:
            cnt +=1
    for top in top10:
        print(top," : ",float(top10[top]))
    return top10


def plot_graph(players,rates):
    plt.bar(players, rates)
    plt.xlabel('Bowlers')
    plt.ylabel('Economy Rate')
    plt.title('Top 10 Economical Bowlers in 2015')
    for i, rate in enumerate(rates):
        plt.text(i, rate, str(rate), ha='center', va='bottom')
    plt.show()


file = open("matches.csv")
delivery = csv.DictReader(file)
first = 0

#firstly get the starting id and ending id of the mathes played in year 2015.
for game in delivery:
    if str(game["season"]) == "2015":
        if(first == 0):
            head = int(game["id"])
            tail = int(game["id"])
            first = 1
        else:
            tail = int(game["id"])
#now move to the deliveries file and then check if it is in range get the bowler details other wise no need to get.

file1 = open("deliveries.csv")
deliveries = csv.DictReader(file1)

bowler_runs = {}
bowler_wickets = {}
bowler_overs = {}
for match in deliveries:
    bowler = match['bowler']
    if((int(match["match_id"]) >= head) and int(match["match_id"])<= tail):
        bowler_runs[match["bowler"]] = bowler_runs.get(bowler,0)+int(match["total_runs"])

        player_dismissed = match['player_dismissed']
        if player_dismissed != "":
            bowler_wickets[bowler] = bowler_wickets.get(bowler, 0) + 1

        # Calculate overs bowled
        ball = match['ball']
        if ball == '1':
            bowler_overs[bowler] = bowler_overs.get(bowler, 0) + 1

#After the score given by each bowler is calculated then find the economy rates of each player
economy_rates = {}
for bowler_name in bowler_overs.keys():
    eco = str(bowler_runs[bowler_name]/bowler_overs[bowler_name])[:4]
    economy_rates[bowler_name] = eco
#sort the economy rates by values and get top 10
sorted_economy_rates = dict(sorted(economy_rates.items(), key=lambda item: float(item[1])))


top10 = get_top10(sorted_economy_rates)

players = list(top10.keys())
rates = list(top10.values())

plot_graph(players,rates)