import matplotlib.pyplot as plt
import csv
from collections import defaultdict
file = open("matches.csv")
delivery = csv.DictReader(file)

teams = {}
for match in delivery:
    year = match["season"]
    team1 = match["team1"]
    team2 = match["team2"]
    #To calcuated the no of games played by each team we need to increment for both the batting team and bowling team.
    #so firstly we will check for year if its present then we will check for each year in that particular year
    #otherwise create an empty dic with that year and add values to it
    #simulatanously do the same thing for both the teams.
    
    
    
    if year not in teams:
        teams[year] = {}
    yearkeys = list(teams[year].keys())


    if team1 not in yearkeys:
        teams[year][team1] = 1
    else:
        teams[year][team1] += 1

    if team2 not in yearkeys:
        teams[year][team2] = 1
    else:
        teams[year][team2] += 1
        



years = list(teams.keys())
group = list(teams[years[0]].keys())

fig, ax = plt.subplots(figsize=(12, 6))

bottom = [0] * len(years)

for te in group:
    team_values = [teams[year].get(te, 0) for year in years]
    ax.bar(years, team_values, label=te, bottom=bottom)
    bottom = [bottom[i] + team_values[i] for i in range(len(years))]

ax.set_xlabel('Year')
ax.set_ylabel('Number of Matches')
ax.set_title('Indian Premier League (IPL) Matches Played by Team (2017-2008)')

plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.tight_layout()
plt.show()



 
