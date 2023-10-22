import csv
from collections import defaultdict
import matplotlib.pyplot as plt


def get_data(path):
    file = open(path)
    data = csv.DictReader(file)
    return data

def get_country_population(data):
    country=["Brunei", "Cambodia", "Indonesia", "Laos", "Malaysia", "Myanmar", "Philippines", "Singapore", "Thailand", "Vietnam"]
    country_population ={}
    #Get the region if the region which we have in Asean countries then add the population to that country.
    #If not present then it means that it is not Asean Country so just go further, and do nothing
    for row in data:
        if(row["Region"] in country and str(row["Year"]) == "2014"):
            country_population[row["Region"]] = country_population.get(row["Region"],0) + int(float(row["Population"]))
    return country_population

def plot_graph(countries,population):
    plt.bar(countries, population)
    plt.xlabel('Country')
    plt.ylabel('Population of the Country')
    plt.title('Asean countries Population')
    plt.xticks(rotation = 45)
    plt.show()

data = get_data("population-estimates_csv.csv")
country_population = get_country_population(data)
countries = list(country_population.keys())
population = list(country_population.values())
plot_graph(countries,population)