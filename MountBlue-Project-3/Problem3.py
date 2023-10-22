
import csv
from collections import defaultdict
import matplotlib.pyplot as plt




def get_data(path):
    file = open(path)
    return csv.DictReader(file)

def get_population(data):
    saarc_population = {}
    countries = ["Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives", "Nepal", "Pakistan", "Sri Lanka"]
    for row in data:
        if row["Region"] in countries:
            saarc_population[row["Year"]] = saarc_population.get(row["Year"],0) + int(float(row["Population"]))

    for i in saarc_population:
        print(i," : ",saarc_population[i])

    return saarc_population

def plot_graph(countries,population):
    plt.bar(countries, population)
    plt.xlabel('Years')
    plt.ylabel('Population of the Country')
    plt.title('Population of SAARC Countries over years')
    plt.xticks(rotation = 45)
    plt.show()

data = get_data("population-estimates_csv.csv")
saarc_population = get_population(data)
countries = list(saarc_population.keys())
population = list(saarc_population.values())
plot_graph(countries,population)