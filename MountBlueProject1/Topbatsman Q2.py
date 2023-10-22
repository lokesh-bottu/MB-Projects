import matplotlib.pyplot as plt
import csv
from collections import defaultdict



def get_data():
    file = open("Deliveries.csv")
    delivery = csv.DictReader(file)
    return delivery


#check for the RCB team first then get the total runs scored by each player 
def get_batsman_scores(delivery):
    batsman_score = {}
    for ball in delivery:
        if(ball["batting_team"] == "Royal Challengers Bangalore"):
            batsman_score[ball["batsman"]] = batsman_score.get(ball["batsman"],0) + int(ball["total_runs"])
    sorted_top_batsman= dict(sorted(batsman_score.items(), key=lambda item:item[1],reverse=True))
    return sorted_top_batsman
#after the score is calculated for each player then sort them by values



#after sorting now get the top 10 batsman by running a loop
def get_top10(sorted_top_batsman):
    top10 = {}
    cnt = 1
    for i in sorted_top_batsman:
        top10[i] = sorted_top_batsman[i]
        if cnt == 10:
            break
        else:
            cnt +=1
    for i in top10:
        print(i," : ",top10[i])
    return top10



def plot_graph(players,rates):
    plt.bar(players, rates)
    plt.xlabel('Batsman')
    plt.ylabel('Runs Scored')
    plt.title('Top 10 Batsman from RCB')
    for i, rate in enumerate(rates):
        plt.text(i, rate, str(rate), ha='center', va='bottom')
    plt.show()


delivery = get_data()
batsman_score = get_batsman_scores(delivery)
top10 = get_top10(batsman_score)

players = list(top10.keys())
rates = list(top10.values())
plot_graph(players,rates)



